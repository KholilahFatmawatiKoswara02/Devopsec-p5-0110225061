from app.storage import TaskStorage
from app.validators import validate_title


class TaskManager:
    def __init__(self, storage=None):
        self.storage = storage or TaskStorage()

    def add_task(self, title: str) -> dict:
        title = validate_title(title)
        return self.storage.add(title)

    def list_tasks(self) -> list:
        return self.storage.all()

    def complete_task(self, task_id: int) -> dict:
        task = self.storage.get(task_id)
        task["completed"] = True
        return task.copy()
