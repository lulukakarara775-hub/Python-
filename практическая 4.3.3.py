a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a == b == c:
    print("равносторонний")
elif a == b or b == c or a == c:
    print("равнобедренный")
else:
    print("разносторонний")