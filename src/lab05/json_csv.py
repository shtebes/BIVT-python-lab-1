import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    Проверка ошибок:
       - неверный тип файла, пустой JSON или CSV → ValueError.
       - осутствующий файл → FileNotFoundError
    """
    jp = Path(json_path)
    if jp.suffix != ".json":
        raise ValueError()  # Неверный тип файла
    if not jp.exists():
        raise FileNotFoundError()  # Файл не найден

    # Читаем файл JSON
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    if len(data) == 0:
        raise ValueError("Пустой JSON")

    all_headers = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError()  # должны быть словарями
        all_headers.update(item.keys())  # добавляем все ключи объекта

    headers = sorted(all_headers)  # сортируем для порядка

    # Запись в CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()

        for item in data:
            # Заполнение отсутствующих полей для каждого объекта
            row = {header: item.get(header, "") for header in headers}
            writer.writerow(row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    cp = Path(csv_path)
    if cp.suffix != ".csv":
        raise ValueError()  # Неверный тип файла
    if not cp.exists():
        raise FileNotFoundError()  # Файл не найден

    # Читаем файл CSV
    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    if len(rows) == 0:
        raise ValueError()  # Пустой CSV

    # Запись в JSON
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=2)


json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_json.csv")
