# ЛР 3
import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")
    for i in ["\t", "\n", "\r"]:
        text = text.replace(i, " ")
    text = " ".join(text.split()).strip()
    return text


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    f = r"\w+(?:-\w+)*"
    allf = re.findall(f, text)
    return allf


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for t in tokens:
        freq_dict[t] = freq_dict.get(t, 0) + 1
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
