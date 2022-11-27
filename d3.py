text = 'Введите номер четверти:'
print(text)
quarter = int(input())
if quarter == 1:
    x = "[1;∞]"
    print(x)
    y = "[1;∞]"
    print(y)
elif quarter == 2:
    x = "[-1;-∞]"
    print(x)
    y = "[1;∞]"
    print(y)
elif quarter == 3:
    x = "[-1;-∞]"
    print(x)
    y = "[-1;-∞]"
    print(y)
elif quarter == 4:
    x = "[1;∞]"
    print(x)
    y = "[-1;-∞]"
    print(y)
elif 0 < quarter or 5 > quarter:
    text1 = 'Введите правильный номер четверти'
    print(text1)