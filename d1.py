text = "Введите номер дня недели"
print(text)
numb_day = int(input())
if 6 > numb_day > 0:
    day_work = 'Нет'
    print(day_work)
elif numb_day > 7:
    null_day = 'В неделе 7 дней'
    print(null_day)
elif 8 > numb_day > 5:
    weekend = 'Да'
    print(weekend)
else:
    wrong = 'Неверное число, введите число от 1 до 7'
    print(wrong)