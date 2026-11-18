import unittest
from task_manager import TaskManager
class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.title, "Finish DevOps lab")
        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertFalse(task.completed)

    def test_complete_task(self):
        task = self.manager.add_task("Submit assignment")
        self.assertTrue(self.manager.complete_task(task.task_id))
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = self.manager.add_task("Read lecture notes")
        self.assertTrue(self.manager.delete_task(task.task_id))
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
if __name__ == "__main__":
    unittest.main()