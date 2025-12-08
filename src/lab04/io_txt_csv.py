from pathlib import Path
import csv
from typing import Iterable, Sequence, Union


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Открывает файл на чтение в указанной кодировке и возвращает содержимое как одну строку
    Аргументы:
       path - путь к файлу (строка или объект Path)
       encoding - кодировка файла, по умолчанию utf-8
    Возвращает:
       данные файла как одну строку
    Ошибки:
       FileNotFoundError: если файл не найден
       UnicodeDecodeError: если кодировка не подходит
    Выбор другой кодировки:
        read_text("file.txt")  # по умолчанию чтение в utf-8
        read_text("file.txt", encoding="cp1251")  # чтение в Windows-1251
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """Создает/перезаписывает CSV с разделителем ","
    Аргументы:
       rows - строки, являющиеся списком/кортежом
       path - путь к файлу
       header - заголовок (необязательный)
    Возвращает: ничего, сохраняет файл
    Ошибки:
       ValueError - если строки в rows не имеют одинаковую длину
    """
    p = Path(path)
    rows = list(rows)
    for i in range(len(rows) - 1):  # проверка на одинаковость длин строк
        if len(rows[i]) != len(rows[i + 1]):
            raise ValueError
    with p.open(
        "w", newline="", encoding="utf-8"
    ) as f:  # открываю файл для записи, newline=""-контролирует, чтобы не было лишних переносов
        w = csv.writer(f)
        if header is not None:
            w.writerow(
                header
            )  # из тз, если передан header, то он записывается первой строкой
        for r in rows:
            w.writerow(r)
