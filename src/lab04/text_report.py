import sys
from pathlib import Path

# sys.path.append('C:\Users\User\Desktop\BIVT-python-lab-1/src')
from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv

sys.path.insert(0, str(Path(__file__).parent.parent))


def main():
    """Читает один входной файл data/lab04/input.txt
    Нормализует текст (lib/text.py), токенизирует и считает частоты слов.
    Сохраняет data/report.csv c колонками: word,count, отсортированными: count ↓, слово ↑ (при равенстве).
    В консоль печатает краткое резюме:
       Всего слов: <N>
       Уникальных слов: <K>
       Топ-5: (список из top_n)
    """

    p = read_text("data/lab04/input.txt")

    normalized_text = normalize(p)
    tokens = tokenize(normalized_text)
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, len(freq_dict))

    write_csv(top_n, "data/lab04/report.csv", ["word", "count"])
    # записывает данные из top в виде csv, в указанный путь, с заголовком

    top_5 = top_n(freq_dict, 5)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")
    for word, count in top_5:
        print(f"{word}:{count}")
