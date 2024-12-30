from datetime import datetime
from exceptions import TaskError

def validate_task_description(description):
    """Проверка, что описание задачи непустое."""
    if not description:
        raise TaskError("Описание задачи не может быть пустым.")

def validate_task_deadline(deadline):
    """Проверка, что формат дедлайна корректен."""
    if deadline:
        try:
            datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            raise TaskError("Некорректный формат дедлайна. Используйте 'ГГГГ-ММ-ДД'.")
