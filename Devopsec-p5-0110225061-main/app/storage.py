class TaskStorage:
    """Store task records in memory."""

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add(self, title: str) -> dict:
        task = {
            "id": self._next_id,
            "title": title,
            "completed": False
        }

        self._tasks.append(task)
        self._next_id += 1

        return task.copy()

    def all(self) -> list:
        return [task.copy() for task in self._tasks]

    def get(self, task_id: int) -> dict:
        for task in self._tasks:
            if task["id"] == task_id:
                return task

        raise KeyError(task_id)
