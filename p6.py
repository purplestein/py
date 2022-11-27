text = "Введите результат первого дня:"
print(text)
a = int(input())
text1 = "Введите желаемый результат:"
print(text1)
b = int(input())
n = 2
day = f"1-й день: {a}"
print(day)
while b > a:
    a = a + (a * 10 / 100)
    a = float('{:.2f}'.format(a))
    days = f"{n}-й день: {a}"
    n += 1
    print(days)
text2 = f"Ответ: на {n - 1}-й день спортсмен достиг результата - не менее {b} км."
print(text2)