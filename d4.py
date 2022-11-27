text_x1 = "Введите координаты х1"
print(text_x1)
x1 = float(input())
text_y1 = "Введите координаты y1"
print(text_y1)
y1 = float(input())
text_x2 = "Введите координаты х2"
print(text_x2)
x2 = float(input())
text_y2 = "Введите координаты y2"
print(text_y2)
y2 = float(input())
c = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
sqrt = c ** (0.5)
sqrt = float('{:.3f}'.format(sqrt))
print(sqrt)