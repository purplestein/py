text = "Введите целое положительное число:"
print(text)
numb = int(input())
numb_max = 0
if numb < 0:
    negative_numb = "Это отрицательное число, попробуйте еще раз"
    print(negative_numb)
while numb > 0:
    numb = numb // 10
    if numb > numb_max:
        numb_max = numb
    print(numb_max)
