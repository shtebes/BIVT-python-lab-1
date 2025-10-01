def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    f_i_o = ' '.join(fio.split()).splt()
    if len(f_i_o) < 2:
        raise ValueError()
    initials = []
    for i in f_i_o[1:]:
        if i:
            initial = i[0].upper() + '.'
            initials.append(initial)
    fio_format = f"{f_i_o[0]} {' '.join(initials)}"
    return f"{fio_format}, гр. {' '.join(group.split())}, GPA {gpa:.2f}"

print(format_record)