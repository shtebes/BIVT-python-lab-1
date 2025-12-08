from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

def main():
    
    # Создаем студентов
    print(" Создание студентов:")
    student1 = Student(
        fio="Попов Кирилл Сергеевич",
        birthdate="2005-01-15",
        group="SE-01",
        gpa=4.5
    )
    
    student2 = Student(
        fio="Петрова Анна Ивановна",
        birthdate="2001-11-23",
        group="CS-02",
        gpa=1.8
    )
    
    print(student1)
    print(student2)
    
    # Проверяем возраст
    print(f"\n Возраст студентов:")
    print(f"{student1.fio}: {student1.age()} лет")
    print(f"{student2.fio}: {student2.age()} лет")
    
    # Сохраняем в JSON
    print("\n Сохранение в файл...")
    students = [student1, student2]
    students_to_json(students, "data/lab08/students_output.json")
    
    # Загружаем из JSON
    print("\n Загрузка из файла...")
    load_students = students_from_json("data/lab08/students_output.json")
    
    # Показываем загруженных студентов
    print("\n Загруженные студенты:")
    for student in load_students:
        print(student)

def test_validation():
    print("\n Проверка валидации:")
    try:
        Student('Тестовый студент', "2009-30-05", "SE-01", 1.0)
    except ValueError as e:
        print(f"Произошла ошибка валидации даты: {e} ")

    try:
        Student("Тестовый студент2", "2008-02-01", "SE-02", 213)
    except ValueError as e:
        print(f"Произошла ошибка валидации GPA: {e} ")

if __name__ == "__main__":
    main()
    test_validation()