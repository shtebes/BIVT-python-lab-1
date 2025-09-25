fio = input("ФИО: ")
fio_no_probel = ' '.join(fio.split())
words = fio_no_probel.split()
a = []
initial = ''.join([i[0].upper() for i in words])
print(f"Инициалы: {initial}.")
print(f"Длина (символов): {len(fio_no_probel)}")