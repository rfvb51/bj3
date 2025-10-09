def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    
    if not isinstance(gpa, (int, float)):
        raise TypeError
    if not fio.strip():
        raise ValueError
    if not group.strip():
        raise ValueError
    
    cleaned_fio = ' '.join(fio.split())
    parts = cleaned_fio.split()
    
    surname = parts[0].title()
    initials = '.'.join(part[0].upper() for part in parts[1:]) + '.'
    
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print('tuples')
print("(\"Иванов Иван Иванович\", \"BIVT-25\", 4.6) ->", format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print("(\"Петров Пётр\", \"IKBO-12\", 5.0) ->", format_record(("Петров Пётр", "IKBO-12", 5.0)))
print("(\" сидорова анна сергеевна \", \"ABB-01\", 3.999) ->", format_record((" сидорова анна сергеевна ", "ABB-01", 3.999)))