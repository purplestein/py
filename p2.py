a = 'Введите время в секундах:'
print(a)
time = int(input())
seconds = time % 3600
minutes = seconds // 60
hours = time // 3600
seconds %= 60
if time < 60:
    print(f"00:00:{time}")
elif 3600 > time >= 60:
    print(f"00:{minutes}:{seconds}")
elif 3600 <= time:
    print(f"{hours}:{minutes}:{seconds}")

