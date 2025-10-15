## Лабораторная работа 1

### _Задание 1_

```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
![скриншот 1](./images/lab01/ex01.png)

### _Задание 2_

```python
a = float(input("a: ").replace(',','.'))
b = float(input("b: ").replace(',','.'))
summa = a + b
avg = summa / 2
print(f"sum={summa:.2f}; avg={avg:.2f}")
```
![скриншот 2](./images/lab01/ex02.png)

### _Задание 3_

```python
price, discount, vat = map(float, input().split())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
![скриншот 3](./images/lab01/ex03.png)

### _Задание 4_

```python
all_minutes = int(input("Минуты: "))
hour = all_minutes // 60
minute = all_minutes % 60
print(f"{hour}:{minute:02d}")
```
![скриншот 4](./images/lab01/ex04.png)

### _Задание 5_

```python
fio = input("ФИО: ").split()
len_fio = 0
for i in fio:
    len_fio += len(i)
print(f"Инициалы: {fio[0][0] + fio[1][0] + fio[2][0]}.")
print(f"Длина (символов): {len_fio + 2}")
```
![скриншот 5](./images/lab01/ex05.png)

### _Задание 6_

```python
kol_player = int(input())
online = 0
offline = 0
for player in range (kol_player):
    stroka = input().split()
    if stroka[-1] == 'True': online+=1
    else: offline+=1
print(online,offline)
```
![скриншот 6](./images/lab01/ex06.png)

### _Задание 7_

```python
stroka = input()
word = ''
ind_1 = -1
ind_2 = -1
flag = 0
for i in range(len(stroka)):
    if stroka[i].isupper() and ind_1 == -1:
        word += stroka[i]
        ind_1 = i
    if stroka[i].isdigit() and ind_2 == -1:
        word += stroka[i + 1]
        ind_2 = i + 1
        ind_pred = ind_2
    if ind_1 > -1 and ind_2 > -1 and flag == 0:
        step = ind_2-ind_1
        if i - ind_pred == step:
            word += stroka[i]
            ind_pred = i
            if stroka[i] == '.':
                print(word)
                flag = 1
```
![скриншот 7](./images/lab01/ex07.png)

## Лабораторная работа 2

### _Задание 1_

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return "ValueError"
    min_zn = nums[0]
    max_zn = nums[0]
    for x in nums[1:]:
        if x < min_zn:
            min_zn = x
        if x > max_zn:
            max_zn = x
    return min_zn, max_zn

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    flat_list = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            return "TypeError"
        for j in i:
            flat_list.append(j)
    return flat_list
```
![скриншот 1](./images/lab02/ex01.png)

### _Задание 2_

```python
def check_rectangular(mat: list[list[float | int]]) -> bool:
    if not mat:
        return True
    len_row_1 = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != len_row_1:
            return False
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    if check_rectangular(mat) == False:
        return "ValueError"
    trans_mat = []
    for j in range (len(mat[0])):
        trans_row = []
        for i in range(len(mat)):
            trans_row.append(mat[i][j])
        trans_mat.append(trans_row)
    return trans_mat

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if check_rectangular(mat) == False:
        return "ValueError"
    sum_mat = []
    for row in mat:
        sum_mat.append(float(sum(row)))
    return sum_mat

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    if check_rectangular(mat) == False:
        return "ValueError"
    sum_mat_2 = []
    for j in range(len(mat[0])):
        col_sum = sum(mat[i][j] for i in range (len(mat)))
        sum_mat_2.append(float(col_sum))
    return sum_mat_2
```
![скриншот 1](./images/lab02/ex02.png)

### _Задание 3_

```python
def format_record(rec: tuple[str, str, float]) -> str:
    if not tuple[0]:
        return "ValueError"
    fio, group, gpa = rec
    fio_f = ' '.join(fio.split()).split()
    if len(fio_f) < 2:
        return "ValueError"
    initials = []
    for i in fio_f[1:]:
        initials.append(i[0].upper() + '.')
    group_f = group.strip()
    if not group_f:
        return "ValueError"
    if gpa < 0:
        return "TypeError"
    return f"{fio_f[0].title()} {''.join(initials)}, гр. {group_f}, GPA {gpa:.2f}"

```
![скриншот 3](./images/lab02/ex03.png)

## Лабораторная работа 3
### Модуль 'src/lib/text.py'
```python
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return("")
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё','е')
        text = text.replace('Ё','Е')
    text = re.sub(r'[\t\r\n]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text: str) -> list[str]:
    if not text:
        return []
    f = r'\w+(?:-\w+)*'
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
```
![скриншот 1](./images/lib/lib1.png)

### Скрипт `src/lab03/text_stats.py`
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
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
    table_mode = os.getenv('TABLE_MODE', '0') == '1'
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
```
![скриншот 2](./images/lab03/ex01.png)

![скриншот 2](./images/lab03/ex02.png)
### Использование
C многострочным вводом: python src/lab03/text_stats.py -> [вводите текст] -> [Ctrl+z для завершения].

Табличный вывод мы используем через переменную окружения: в терминале -> $env:TABLE_MODE=1; python src/lab03/text_stats.py (для включения таблицы). Для обычного вывода - простое python src/lab03/text_stats.py, так как по умолчанию табличный вывод выключен.