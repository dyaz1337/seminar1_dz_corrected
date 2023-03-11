#Задание 2
print("Введите время в секундах: ")
time = int(input())
minutes = time / 60
hour = minutes / 60
print(f"Время в формате ч:м:с - {hour} : {minutes} : {time}")