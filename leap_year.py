try:
    def leap_year():
        year = int(input("Введите год: "))

        if year % 4 == 0 and year % 400 == 0:
            print("Год является високосным.")
        else:
            print("Год не является високосным.")

except ValueError:
    print('Вводите только год и без пробелов!')

else:
    leap_year()