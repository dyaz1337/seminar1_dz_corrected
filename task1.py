#Задание 1
name = input("Введите ваше имя: ")
password = input("Введите ваш пароль: ")
age = input("Введите ваш возраст: ")
if name.isnumeric():
    print("Имя не может состоять из одних цифр")
if age.isnumeric() == False:
    print("Возраст не может содержать буквенное значение")
else:
      print(f"Ваши данные для входа в аккаунт: "
      f"имя - {name}, "
      f"пароль - {password}, "
      f"возраст - {age}")
