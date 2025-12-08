def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple) or len(rec) != 3:
        return ValueError()
    if not isinstance(rec[0], str):
        raise TypeError()
    if not isinstance(rec[1], str):
        raise TypeError()
    if not isinstance(rec[2], (int, float)):
        raise TypeError()

    fio, group, gpa = rec
    fio_f = " ".join(fio.split()).split()
    if len(fio_f) < 2:
        return "ValueError"
    initials = []
    for i in fio_f[1:]:
        initials.append(i[0].upper() + ".")
    group_f = group.strip()
    if not group_f:
        return "ValueError"
    if gpa < 0:
        return "TypeError"
    return f"{fio_f[0].title()} {''.join(initials)}, гр. {group_f}, GPA {gpa:.2f}"


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "ABB-01", 3.999)))
print(format_record(("  сидорова  анна   сергеевна ", "  ", 3.999)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", -3.999)))
