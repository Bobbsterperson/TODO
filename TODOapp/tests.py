from django.test import TestCase
from django.urls import reverse
from .models import TODO

class PassingTests(TestCase):
    def setUp(self):
        TODO.objects.create(title="Task 1", Notes="Notes for Task 1", category="Category A", completed=False)
        TODO.objects.create(title="Task 2", Notes="Notes for Task 2", category="Category B", completed=True)
        TODO.objects.create(title="Task 3", Notes="Notes for Task 3", category="Category C", completed=False)

    def test_mark_complete_function(self):
        """Test marking a TODO item as complete."""
        task = TODO.objects.get(title="Task 1")
        response = self.client.get(reverse('task-complete', args=[task.id]))
        task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertTrue(task.completed)

    def test_mark_incomplete_function(self):
        """Test marking a TODO item as incomplete."""
        task = TODO.objects.get(title="Task 2")
        response = self.client.get(reverse('task-incomplete', args=[task.id]))
        task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(task.completed)

    def test_task_list(self):
        """Test that the task list view shows the tasks correctly."""
        response = self.client.get(reverse('TODOs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")
        self.assertContains(response, "Task 3")

    def test_task_detail(self):
        """Test that the task detail view shows the correct task."""
        task = TODO.objects.get(title="Task 1")
        response = self.client.get(reverse('task_detail', args=[task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Task: Task 1")
        self.assertContains(response, "Notes: Notes for Task 1")

    def test_task_create(self):
        """Test creating a new task."""
        response = self.client.post(reverse('task-create'), {
            'title': 'Task 4',
            'Notes': 'Notes for Task 4',
            'category': 'Category D',
            'completed': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(TODO.objects.filter(title="Task 4").exists())

    def test_task_update(self):
        """Test updating an existing task."""
        task = TODO.objects.get(title="Task 1")
        response = self.client.post(reverse('task-update', args=[task.id]), {
            'title': 'Updated Task 1',
            'Notes': 'Updated Notes for Task 1',
            'category': 'Updated Category A',
            'completed': True
        })
        self.assertEqual(response.status_code, 302)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task 1')
        self.assertTrue(task.completed)

    def test_task_delete(self):
        """Test deleting an existing task."""
        task = TODO.objects.get(title="Task 1")
        response = self.client.post(reverse('task_confirm_delete', args=[task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TODO.objects.filter(title="Task 1").exists())


class FailingTests(TestCase):

    def setUp(self):
        TODO.objects.create(title="Sample Task", Notes="Some notes", created_at="2024-01-01", category="General", completed=False)

    def test_todo_creation_fail(self):
        """Intentionally failing test case."""
        task = TODO.objects.get(title="Sample Task")
        self.assertEqual(task.category, "Nonexistent Category")  # This will fail

    def test_todo_list_view_fail(self):
        """Intentionally failing test case."""
        response = self.client.get(reverse('TODOs'))
        self.assertContains(response, "Nonexistent Task")  # This will fail

    def test_todo_detail_view_fail(self):
        """Intentionally failing test case."""
        task = TODO.objects.get(title="Sample Task")
        response = self.client.get(reverse('task_detail', args=[task.id]))
        self.assertContains(response, "Nonexistent Detail")  # This will fail
