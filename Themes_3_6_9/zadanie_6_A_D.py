# Напишите программу, которая создает пустой список и 
# заполняет его случайными элементами. 
# Затем программа выводит элементы списка в обратном порядке.

import random

class RandomListApp:
    def __init__(self):
        self.random_list = []
        self.menu_options = {
            '1': self.fill_list,
            '2': self.display_reverse,
            '3': self.exit_program
        }

    def greet_user(self):
        print("Добро пожаловать в программу заполнения списка случайными числами!")
        print("Вы можете заполнить список, отобразить его в обратном порядке или выйти из программы.")

    def fill_list(self):
        try:
            size = int(input("Введите количество элементов для заполнения списка: "))
            if size <= 0:
                raise ValueError("Количество элементов должно быть положительным.")
            self.random_list = [random.randint(1, 100) for _ in range(size)]
            print(f"Список успешно заполнен: {self.random_list}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def display_reverse(self):
        if not self.random_list:
            print("Список пуст. Сначала заполните его.")
        else:
            reversed_list = self.random_list[::-1]
            print(f"Список в обратном порядке: {reversed_list}")

    def exit_program(self):
        print("Спасибо за использование программы! До свидания!")
        exit()

    def show_menu(self):
        while True:
            print("nМеню:")
            print("1. Заполнить список случайными числами")
            print("2. Показать список в обратном порядке")
            print("3. Выход")
            choice = input("Выберите опцию (1-3): ")

            action = self.menu_options.get(choice)
            if action:
                action()
            else:
                print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 3.")

if __name__ == "__main__":
    app = RandomListApp()
    app.greet_user()
    app.show_menu()
