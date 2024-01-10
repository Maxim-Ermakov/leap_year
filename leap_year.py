def leap_year():
    year = int(input("Введите год: "))

    if year // 4 and year // 100:
        print("Год является високосным.")
    else:
        print("Год не является високосным.")


leap_year()