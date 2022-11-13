money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
a = money_capital
while a >= spend:
    spend *= (1+increase)
    month += 1
    a = a - (spend - salary)
print(month)
