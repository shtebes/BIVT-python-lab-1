import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
from text import normalize, tokenize, count_freq, top_n


def print_table(top_words, total_words, unique_words):
    max_len = max(len(word) for word, i in top_words)
    column_width = max(max_len, 6)
    table_width = column_width + 15
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 самых частых слов:")

    print("┌" + "─" * (column_width + 2) + "┬" + "─" * 12 + "┐")
    print(f"│ { 'Слово':<{column_width}} │ {'Частота':<10} │")
    print("├" + "─" * (column_width + 2) + "┼" + "─" * 12 + "┤")

    for word, freq in top_words:
        print(f"│ {word:<{column_width}} │ {freq:<10} │")
    print("└" + "─" * (column_width + 2) + "┴" + "─" * 12 + "┘")


def main():
    table_mode = os.getenv("TABLE_MODE", "0") == "1"
    text = sys.stdin.read().strip()
    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq_dict = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)
    if table_mode:
        print_table(top_words, total_words, unique_words)
    else:
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_words:
            print(f"{word}:{count}")


if __name__ == "__main__":
    main()
