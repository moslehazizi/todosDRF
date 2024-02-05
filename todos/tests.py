from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "First test todo",
            body = "Todo body for test", 
        )
    
    def test_model_content(self):
        self.assertEqual(self.todo.title, "First test todo")
        self.assertEqual(self.todo.body, "Todo body for test")
        self.assertEqual(str(self.todo), "First test todo")