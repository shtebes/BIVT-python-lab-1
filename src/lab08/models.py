from dataclasses import dataclass
from datetime import datetime, date
import re

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # проверяет данные
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неправильный формат даты: {self.birthdate}. Нужно: ГГГГ-ММ-ДД")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть от 0 до 5, а у вас: {self.gpa}")

    def age(self) -> int:
        # вернуть количество полных лет
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        if (today.month, today.day) < (birth.month, birth.day):
            return today.year - birth.year -1
        return today.year - birth.year

    def to_dict(self) -> dict:
        # сериализация
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group":self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        # десереализация из словаря
        return cls(
            fio = d["fio"],
            birthdate = d["birthdate"],
            group = d["group"],
            gpa = d["gpa"]
        )

    def __str__(self) -> str:
        # красивый вывод
        return f"{self.fio}: группа: {self.group}, возраст: {self.age()}, GPA: {self.gpa}"