from datetime import datetime
from validation import validate_task_description, validate_task_deadline  

class Task:
    def __init__(self, description, deadline=None, completed=False):
        """
        Инициализация задачи.

        :param description: Описание задачи.
        :param deadline: Дедлайн задачи в формате 'ГГГГ-ММ-ДД' (по умолчанию None).
        :param completed: Статус завершенности задачи (по умолчанию False).
        :raises TaskError: Если описание задачи пустое или дедлайн указан в некорректном формате.
        """
        validate_task_description(description)  # Проверка описания
        validate_task_deadline(deadline)  # Проверка дедлайна

        self.description = description
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d') if deadline else None
        self.completed = completed

    def mark_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def to_dict(self):
        """Преобразовать задачу в словарь для сохранения в JSON.

        :return: Словарь с полями 'description', 'deadline' и 'completed'.
        """
        return {
            'description': self.description,
            'deadline': self.deadline.strftime('%Y-%m-%d') if self.deadline else None,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        """Создать экземпляр задачи из словаря.

        :param data: Словарь с данными задачи.
        :return: Экземпляр класса Task.
        """
        deadline = data.get('deadline')
        return cls(data['description'], deadline, data['completed'])
