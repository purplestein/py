text = 'Введите координаты х'
print(text)
x = int(input())
text1 = 'Введите координаты y'
print(text1)
y = int(input())
if x > 0 and y > 0:
    quarter1 = 1
    print(quarter1)
elif x < 0 and y > 0:
    quarter2 = 2
    print(quarter2)
elif x < 0 and y < 0:
    quarter3 = 3
    print(quarter3)
elif x > 0 and y < 0:
    quarter4 = 4
    print(quarter4)
elif x == 0 and y == 0:
    text2 = 'Координаты неверные'
    print(text2)