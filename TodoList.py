import json
import os
from exceptions import TodoListError
from Task import Task
from validation import validate_task_description, validate_task_deadline

class TodoList:
    def __init__(self, filename='tasks.json'):
        """
        Инициализация списка задач и загрузка из файла.

        :param filename: Имя файла для сохранения и загрузки задач.
        """
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, description, deadline=None):
        """Добавить новую задачу в список.

        :param description: Описание задачи, которую необходимо добавить.
        :param deadline: Дедлайн задачи в формате 'ГГГГ-ММ-ДД'.
        :raises TaskError: Если описание задачи пустое или дедлайн указан в некорректном формате.
        """
        validate_task_description(description)  # Валидация описания
        validate_task_deadline(deadline)  # Валидация дедлайна

        task = Task(description, deadline)  # Создание задачи с проверенными параметрами
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        """Удалить задачу по индексу.

        :param index: Индекс задачи, которую нужно удалить.
        :raises TodoListError: Если индекс вне диапазона.
        """
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
        else:
            raise TodoListError("Индекс вне диапазона!")

    def view_tasks(self):
        """Просмотреть все задачи в виде таблицы."""
        if not self.tasks:
            print("Все задачи выполнены! Good job✨")
            print(' ∧,,,∧')
            print('( •·• )')
            print ('/づ♡ I love you')
            return

        print(f"\n{'№':<5}{'Описание задачи':<30}{'Дедлайн':<12}{'Статус':<10}")
        print("-" * 50)
        for index, task in enumerate(self.tasks):
            status = "✔️" if task.completed else "❌"
            deadline = task.deadline.strftime('%Y-%m-%d') if task.deadline else ""
            print(f"{index + 1:<5}{task.description:<30}{deadline:<12}{status:<10}")

    def mark_task_completed(self, index):
        """Пометить задачу как выполненную.

        :param index: Индекс задачи, которую нужно завершить.
        :raises TodoListError: Если индекс вне диапазона.
        """
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()
        else:
            raise TodoListError("Индекс вне диапазона!")

    def save_tasks(self):
        """Сохранить задачи в файл в формате JSON."""
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f)

    def load_tasks(self):
        """Загрузить задачи из файла."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task) for task in tasks_data]
