#Задание 4
earnings = int(input("Введите выручку фирмы: "))
cost = int(input("Введите издержки фирмы: "))
result = earnings - cost

if cost > 0:
    print(f"Финансовый результат - прибыль. Её величина: {result}")
elif earnings == cost:
    print("Финансовый результат - безприбыльность")
else:
    print(f"Финансовый результат - убыток. Её величина: {result}")

profitability = result / earnings
print(f"Рентабельность выручки = {profitability}")

strength = int(input("Введите численность сотрудников фирмы: "))
company_profit = result / strength
print(f"Прибыль фирмы в расчете на одного сотрудника = {company_profit}")