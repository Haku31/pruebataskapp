import tornado.web
import tornado.escape
import json
from app.models import Task, TaskStore

# Global instance for storing tasks
task_store = TaskStore()

class TaskHandler(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.task_store = kwargs.pop('task_store', None)
        super(TaskHandler, self).__init__(*args, **kwargs)
        
    def get(self, task_id=None):
        try:
            if task_id:
                task = task_store.tasks.get(task_id)
                if task:
                    self.set_header("Content-Type", "application/json")
                    self.set_header("Access-Control-Allow-Origin", "*")
                    self.write(json.dumps(task.__dict__))
                else:
                    self.set_status(404)
                    self.set_header("Access-Control-Allow-Origin", "*")
                    self.write({
                        "error": "Task not found"
                    })
            else:
                tasks = task_store.get_all_tasks()
                self.set_header("Content-Type", "application/json")
                self.set_header("Access-Control-Allow-Origin", "*")
                self.write(json.dumps([task.__dict__ for task in tasks]))
        except Exception as e:
            self.set_status(500)
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({
                "error": "An error occurred while fetching tasks.",
                "details": str(e)
            })

    def post(self):
        try:
            task_data = tornado.escape.json_decode(self.request.body)
            if not all(k in task_data for k in ("title", "description", "completed")):
                self.set_status(400)
                self.set_header("Access-Control-Allow-Origin", "*")
                self.write({
                    "error": "Missing required fields: title, description, or completed."
                })
                return

            new_task = Task(
                title=task_data["title"],
                description=task_data["description"],
                completed=task_data["completed"]
            )
            created_task = task_store.add_task(new_task)
            self.set_header("Content-Type", "application/json")
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write(json.dumps(created_task.__dict__))
            self.set_status(201)
        except json.JSONDecodeError:
            self.set_status(400)
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({
                "error": "Invalid JSON format."
            })
        except Exception as e:
            self.set_status(500)
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({
                "error": "An error occurred while creating a task.",
                "details": str(e)
            })

    def put(self, task_id):
        try:
            task_data = tornado.escape.json_decode(self.request.body)
            if not all(k in task_data for k in ("title", "description", "completed")):
                self.set_status(400)
                self.set_header("Access-Control-Allow-Origin", "*")
                self.write({
                    "error": "Missing required fields: title, description, or completed."
                })
                return

            updated_task = Task(
                title=task_data["title"],
                description=task_data["description"],
                completed=task_data["completed"]
            )
            updated_task.id = task_id  # Make sure to set the id for updating
            task = task_store.update_task(task_id, updated_task)
            if task:
                self.set_header("Content-Type", "application/json")
                self.set_header("Access-Control-Allow-Origin", "*")
                self.write(json.dumps(task.__dict__))
            else:
                self.set_status(404)
                self.set_header("Access-Control-Allow-Origin", "*")
                self.write({
                    "error": "Task not found"
                })
        except json.JSONDecodeError:
            self.set_status(400)
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({
                "error": "Invalid JSON format."
            })
        except Exception as e:
            self.set_status(500)
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({
                "error": "An error occurred while updating the task.",
                "details": str(e)
            })

    def delete(self, task_id):
        try:
            task = task_store.delete_task(task_id)
            if task:
                self.set_status(204)
                self.set_header("Access-Control-Allow-Origin", "*")
            else:
                self.set_status(404)
                self.set_header("Access-Control-Allow-Origin", "*")
                self.write({
                    "error": "Task not found"
                })
        except Exception as e:
            self.set_status(500)
            self.set_header("Access-Control-Allow-Origin", "*")
            self.write({
                "error": "An error occurred while deleting the task.",
                "details": str(e)
            })

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.finish()
