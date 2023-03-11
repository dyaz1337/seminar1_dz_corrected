#Задание 3
num = int(input("Введите целое положительное число: "))
if num < 0:
    print("Это не положительное число. Попробуйте еще раз :)")
else:
    total = (num + int(str(num) + str(num)) + int(
        str(num) + str(num) + str(num)))
    print(f"Сумма чисел {num} + {num * 11} + {num * 111} = %d" % total)
