text1 = "Введите сумму выручки:"
print(text1)
revenue = int(input())
text2 = "Введите сумму издержек:"
print(text2)
costs = int(input())
if revenue > costs:
    text_revenue = "Фирма прибыльная"
    print(text_revenue)
    profit = f"Рентабельность фирмы равна {revenue / costs * 100}%"
    print(profit)
    text3 = "Введите количество сотрудников:"
    print(text3)
    staff = int(input())
    rev_staff = f"Прибыль на одного сотрудника фирмы: {revenue / staff}"
    print(rev_staff)
elif revenue == costs:
    text_null = "Фирма работает в ноль"
    print(text_null)
else:
    text_costs = "Фирма убыточная"
    print(text_costs)

