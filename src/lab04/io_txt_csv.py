from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    path = Path(path)
    rows = list(rows)
    
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError() 
    path.parent.mkdir(parents=True, exist_ok=True)#ошибка длин строк
    
    with path.open("w", newline="", encoding="utf-8") as file: #w - открыть для записи
        w = csv.writer(file)
        w.writerows(rows) #записываю все строки данных в файл


def ensure_parent_dir(path):#создание папок
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

