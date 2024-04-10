import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
django.setup()

from todo_app.models import Todo

fake = Faker()

def create_todos(n=100):
    for _ in range(n):
        Todo.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.text(),
            completed=fake.boolean()
        )

if __name__ == '__main__':
    print('Populating script!')
    create_todos(100)
    print('Populating complete!')
