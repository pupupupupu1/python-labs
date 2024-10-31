#money_capital = 20000  # Подушка безопасности
#salary = 5000  # Ежемесячная зарплата
#spend = 6000  # Траты за первый месяц
#increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

#print("Количество месяцев, которое можно протянуть без долгов:", ...)

money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
months_without_debt = 0

while money_capital > 0:
    budget = salary + money_capital
    if spend > budget:
        break
    money_capital = budget - spend
    spend = spend * (1 + increase)
    months_without_debt += 1

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)
