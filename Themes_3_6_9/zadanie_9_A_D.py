# Создайте класс "Студент", который содержит атрибуты "имя" и "возраст". 
# Создайте объекты этого класса, представляющие 
# разных студентов, и выведите информацию о них.

import sqlite3
from typing import List

# Декоратор для отображения информации о студенте
def student_info_decorator(func):
    def wrapper(student):
        result = func(student)
        print(f"Информация о студенте: {result}")
        return result
    return wrapper

# Базовый класс для студентов
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @student_info_decorator
    def __str__(self) -> str:
        return f"Имя: {self.name}, Возраст: {self.age}"

# Класс для управления базой данных студентов
class StudentDatabase:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
            """)

    def add_student(self, student: Student):
        with self.connection:
            self.connection.execute("INSERT INTO students (name, age) VALUES (?, ?)", 
                                    (student.name, student.age))

    def get_all_students(self) -> List[Student]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT name, age FROM students")
        rows = cursor.fetchall()
        return [Student(name=row[0], age=row[1]) for row in rows]

    def close(self):
        self.connection.close()

# Главное приложение
class StudentApp:
    def __init__(self):
        self.db = StudentDatabase("students.db")
        self.greet_user()

    def greet_user(self):
        print("Добро пожаловать в программу управления студентами!")
        print("Вы можете добавлять студентов и просматривать их информацию.")

    def show_menu(self):
        while True:
            print("nМеню:")
            print("1. Добавить студента")
            print("2. Показать всех студентов")
            print("3. Выход")
            choice = input("Выберите опцию (1-3): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.exit_program()
            else:
                print("Неверный выбор. Пожалуйста, выберите опцию от 1 до 3.")

    def add_student(self):
        name = input("Введите имя студента: ")
        age = int(input("Введите возраст студента: "))
        student = Student(name, age)
        self.db.add_student(student)
        print(f"Студент {student.name} добавлен в базу данных.")

    def display_students(self):
        students = self.db.get_all_students()
        if not students:
            print("Нет студентов в базе данных.")
        else:
            for student in students:
                print(student)

    def exit_program(self):
        print("Спасибо за использование программы! До свидания!")
        self.db.close()
        exit()

if __name__ == "__main__":
    app = StudentApp()
    app.show_menu()