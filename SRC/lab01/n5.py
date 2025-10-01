fullname = input("ФИО: ")
newname = ' '.join(fullname.split())

words = newname.split()
initials = ''.join(word[0].upper() for word in words)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(newname)}")