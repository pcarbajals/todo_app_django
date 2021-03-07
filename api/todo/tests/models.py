from django.test import TestCase
from todo.models import Task

class TaskTestCase(TestCase):
    ''' Test cases for the Task model '''

    def test_model_str_return_title(self):
        t = Task.objects.create(title='Task with title')
        self.assertEqual(str(t), 'Task with title')

    def test_default_values(self):
        t = Task.objects.create()
        self.assertEqual(t.status.label, 'To Do')
