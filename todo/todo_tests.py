from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    def test_create_todo(self):
        todo = Todo.objects.create(title="テスト", completed=False)
        self.assertEqual(todo.title, "テスト")
        self.assertFalse(todo.completed)