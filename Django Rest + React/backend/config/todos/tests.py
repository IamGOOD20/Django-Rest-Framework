from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='a body here')

    def test_title_content(self):
        '''Test: looking for a title '''
        todo = Todo.objects.get(id=1)
        expected_object_name = todo.title
        self.assertEqual(expected_object_name, 'first todo')

    def test_body_content(self):
        '''Test: looking for a body'''
        todo = Todo.objects.get(id=1)
        expected_object_name = todo.body
        self.assertEqual(expected_object_name, 'a body here')
