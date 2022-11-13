salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
a = 1
while months >= a:
    a += 1
    i = spend - salary
    spend *= (1 + increase)
    need_money += i
print(round(need_money))
