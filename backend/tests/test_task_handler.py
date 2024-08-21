import tornado.ioloop
import tornado.web
import tornado.testing
import json
from app.handlers.task_handler import TaskHandler
from app.models import Task, TaskStore
class TestApp(tornado.testing.AsyncHTTPTestCase):
    
    def get_app(self):
        self.task_store = TaskStore()
        return tornado.web.Application([
            (r"/tasks", TaskHandler, dict(task_store=self.task_store)),
            (r"/tasks/([0-9a-fA-F\-]+)", TaskHandler, dict(task_store=self.task_store)),
        ])

    def test_create_task(self):
        response = self.fetch(
            '/tasks',
            method='POST',
            body=json.dumps({
                'title': 'Test Task',
                'description': 'Test Description',
                'completed': False
            }),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.code, 201)
        response_body = json.loads(response.body)
        self.assertIn('id', response_body)
        self.task_id = response_body['id']  # Store ID for later tests

    def test_get_task(self):
        if not hasattr(self, 'task_id'):
            self.test_create_task()
        response = self.fetch(f'/tasks/{self.task_id}')
        self.assertEqual(response.code, 200)
        response_body = json.loads(response.body)
        self.assertEqual(response_body['id'], self.task_id)

    def test_get_all_tasks(self):
        self.test_create_task()
        response = self.fetch('/tasks')
        self.assertEqual(response.code, 200)
        response_body = json.loads(response.body)
        self.assertGreater(len(response_body), 0)

    def test_update_task(self):
        if not hasattr(self, 'task_id'):
            self.test_create_task()
        response = self.fetch(
            f'/tasks/{self.task_id}',
            method='PUT',
            body=json.dumps({
                'title': 'Updated Task',
                'description': 'Updated Description',
                'completed': True
            }),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.code, 200)
        response_body = json.loads(response.body)
        self.assertEqual(response_body['title'], 'Updated Task')
        self.assertEqual(response_body['completed'], True)

    def test_delete_task(self):
        if not hasattr(self, 'task_id'):
            self.test_create_task()
        response = self.fetch(f'/tasks/{self.task_id}', method='DELETE')
        self.assertEqual(response.code, 204)

    def test_get_nonexistent_task(self):
        response = self.fetch('/tasks/nonexistent-id')
        self.assertEqual(response.code, 404)

    def test_create_task_invalid_json(self):
        response = self.fetch(
            '/tasks',
            method='POST',
            body='Invalid JSON',
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.code, 400)

    def test_update_task_invalid_json(self):
        if not hasattr(self, 'task_id'):
            self.test_create_task()
        response = self.fetch(
            f'/tasks/{self.task_id}',
            method='PUT',
            body='Invalid JSON',
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(response.code, 400)

    def test_options_request(self):
        response = self.fetch('/tasks', method='OPTIONS')
        self.assertEqual(response.code, 204)
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Methods'),
            'GET, POST, PUT, DELETE, OPTIONS'
        )
        self.assertEqual(
            response.headers.get('Access-Control-Allow-Headers'),
            'Content-Type'
        )
