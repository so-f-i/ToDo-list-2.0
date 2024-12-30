from TodoList import TodoList
from exceptions import TodoListError

def main():
    todo_list = TodoList()
    while True:
        print("\n🔧 Действия: 1 - Добавить, 2 - Удалить, 3 - Просмотреть, 4 - Завершить, 5 - Выход")
        choice = input("Выберите действие (1-5): ")

        try:
            if choice == '1':
                task_desc = input("🦋☆*: .｡. Введите описание задачи .｡.:*☆🦋")
                deadline = input("📅Введите дедлайн задачи (ГГГГ-ММ-ДД) или оставьте пустым: ")
                todo_list.add_task(task_desc, deadline)
            elif choice == '2':
                todo_list.view_tasks()
                index = int(input("✧.｡.Введите номер задачи для удаления.｡.✧ ")) - 1
                todo_list.remove_task(index)
            elif choice == '3':
                todo_list.view_tasks()
            elif choice == '4':
                todo_list.view_tasks()
                index = int(input("✧.｡.Введите номер задачи для завершения.｡.✧ ")) - 1
                todo_list.mark_task_completed(index)
            elif choice == '5':
                print("❤️⸜(˶˃ ᵕ ˂˶)⸝❤️ Выход из программы")
                break
            else:
                print("😥 Пожалуйста, выберите корректное действие")
        except (TodoListError, ValueError) as e:
            print(f"😥Ошибка😥: {e}")

if __name__ == "__main__":
    main()
