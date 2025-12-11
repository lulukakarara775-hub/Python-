filename = input("Введите имя файла с расширением: ").lower()
if filename.endswith(".doc"):
    print("Word file")
elif filename.endswith(".py"):
    print("Python file")
elif filename.endswith(".txt"):
    print("Text file")
else:
    print("Неизвестное расширение")