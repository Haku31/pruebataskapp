import uuid

class Task:
    def __init__(self, title, description, completed=False):
        self.id = str(uuid.uuid4())  # Generación de un UUID único
        self.title = title
        self.description = description
        self.completed = completed

class TaskStore:
    def __init__(self):
        self.tasks = {}

    def get_all_tasks(self):
        return self.tasks.values()

    def add_task(self, task):
        self.tasks[task.id] = task
        return task

    def update_task(self, task_id, updated_task):
        if task_id in self.tasks:
            current_task = self.tasks[task_id]
            current_task.title = updated_task.title
            current_task.description = updated_task.description
            current_task.completed = updated_task.completed
            return current_task
        return None

    def delete_task(self, task_id):
        return self.tasks.pop(task_id, None)
