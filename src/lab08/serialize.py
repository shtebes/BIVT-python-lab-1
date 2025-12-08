import json
from .models import Student

def students_to_json(students, path):
    "Сохранение списка студентов в JSON файл."
    data = [student.to_dict() for student in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)

    print(f"Данные сохранены в файл: {path}")

def students_from_json(path: str) -> list[Student]:
    "Загрузка списка студентов из JSON файла."
  
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = [Student.from_dict(item) for item in data]
        
        print(f"Загружено {len(students)} студентов из файла: {path}")
        return students
    
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка в формате JSON файла: {path}")
        return []