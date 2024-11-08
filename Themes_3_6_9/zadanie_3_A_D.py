# Напишите программу, которая запрашивает у пользователя его имя, а затем выводит 
# приветственное сообщение с использованием этого имени


class GreetingApp:
    def __init__(self):
        self.user_name = ""

    def get_user_name(self):
        while True:
            try:
                name = input("Введите ваше имя: ").strip()
                if not name:
                    raise ValueError("Имя не может быть пустым.")
                self.user_name = name
                break
            except ValueError as e:
                print(e)

    def display_greeting(self):
        print(f"Здравствуйте, {self.user_name}! Добро пожаловать в нашу программу.")

    def show_menu(self):
        while True:
            print("nМеню:")
            print("1. Ввести имя")
            print("2. Показать приветствие")
            print("3. Выход")
            choice = input("Выберите опцию (1-3): ")

            if choice == '1':
                self.get_user_name()
            elif choice == '2':
                if self.user_name:
                    self.display_greeting()
                else:
                    print("Сначала введите ваше имя.")
            elif choice == '3':
                print("Спасибо за использование программы! До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 3.")

if __name__ == "__main__":
    app = GreetingApp()
    app.show_menu()
