import csv
from pathlib import Path
from datetime import datetime
from typing import List, Optional

from models import Student


class Group:

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 
    
    def _ensure_storage_exists(self):
        """Создание файла с заголовком, если его нет"""
        if not self.path.exists():
            # Создаем директорию, если её нет
            self.path.parent.mkdir(parents=True, exist_ok=True)
            # Создаем файл с заголовком
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
    
    def _read_all(self) -> List[dict]:
        """Чтение всех записей из CSV файла"""
        students = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row:  
                        students.append(row)
        except FileNotFoundError:
            self._ensure_storage_exists()
        return students
    
    def _write_all(self, students: List[dict]):
        """Запись всех студентов в CSV файл"""
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(students)
    
    def list(self) -> List[Student]:
        """ Получение всех студентов группы """
        data = self._read_all()
        return [Student.from_dict(item) for item in data]
    
    def add(self, student: Student):
        """Добавление нового студента"""
        students = self._read_all()
        for s in students:
            if s['fio'] == student.fio:
                print(f"Студент {student.fio} уже существует!")
                return False
        students.append(student.to_dict())
        self._write_all(students)
        return True
    
    def find(self, substr: str) -> List[Student]:
        """Поиск студентов по подстроке в ФИО"""
        all_students = self.list()
        result = []
        for student in all_students:
            if substr.lower() in student.fio.lower():
                result.append(student)
        return result
    
    def remove(self, fio: str) -> bool:
        """Удаление студента по ФИО"""
        students = self._read_all()
        initial_count = len(students)
        students = [s for s in students if s['fio'] != fio]
    
        if len(students) < initial_count:
            self._write_all(students)
            return True
        return False
    
    def update(self, fio: str, **fields) -> bool:
        """Обновление полей существующего студента"""
        students = self._read_all()
        updated = False
        
        for student in students:
            if student['fio'] == fio:
                for field, value in fields.items():
                    if field in ['fio', 'birthdate', 'group', 'gpa']:
                        if field == 'gpa':
                            student[field] = str(float(value))
                        else:
                            student[field] = value
                updated = True
                break
        if updated:
            self._write_all(students)
        return updated
    
    def stats(self) -> dict:
        """Статистика по группе (дополнительное задание со звёздочкой)"""
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }

        gpa_values = [float(s.gpa) for s in students]
        groups_dict = {}
        
        for student in students:
            group_name = student.group
            if group_name in groups_dict:
                groups_dict[group_name] += 1
            else:
                groups_dict[group_name] = 1
        
        # Топ-5 студентов по GPA
        sorted_students = sorted(students, key=lambda x: x.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_dict,
            "top_5_students": top_5
        }



if __name__ == "__main__":
    group = Group("data/lab09/students.csv")

    new_student = Student("Павлова Аина Егоровна", "2013-08-23", "БИВТ-25-4", 4.8)
    group.add(new_student)

    new_student = Student("Козлов Алексей Викторович", "2003-08-12", "БИВТ-21-3", 4.5)
    group.add(new_student)
    
    # Пример 2: Поиск студентов
    found_students = group.find("анн")
    for student in found_students:
        print(student)  # Найдет Сидорову Анну
        
    # Пример 3: Обновление данных
    group.update("Сидорова Анна Сергеевна", gpa=4.9, group="БИВТ-21-2")
    
    # Пример 4: Удаление
    group.remove("Иванов Иван Иванович")
    
    # Пример 5: Получение статистики
    print("\n",group.stats())
