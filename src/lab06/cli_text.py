import argparse
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной работы 6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумерация строк")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Входной текстовый файл")
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    file = Path(args.input)

    if args.command == "cat":
        " вывод содержимого файла построчно (с нумерацией при -n). "

        with open(file, "r", encoding="utf-8") as f:
            number = 1
            for row in f:
                row = row.rstrip("\n") 
                if args.n: # при указанном флаге выводятся пронумерованные строки
                    print(f"{number}. {row}")
                    number += 1
                else:
                    print(row)
    
    elif args.command == "stats":
        " анализ частот слов в тексте "
        with open(file, "r", encoding="utf-8") as f:
            data = [row for row in f]
        data = "".join(data)
        tokens = tokenize(text=data)
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)

        print(f"Топ-{args.top} слов в файле '{args.input}':")
        number = 1
        for x, y in top:
            print(f"{number}. '{x}' - {y}")
            number += 1

if __name__ == "__main__":
    main()