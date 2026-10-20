import unittest

from app.task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Python")
        self.assertEqual(task["title"], "Study Python")

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(" ")

    def test_complete_task(self):
        task = self.manager.add_task("Finish assignment")
        result = self.manager.complete_task(task["id"])
        self.assertTrue(result["completed"])

    def test_unknown_task(self):
        with self.assertRaises(KeyError):
            self.manager.complete_task(999)


if __name__ == "__main__":
    unittest.main()
