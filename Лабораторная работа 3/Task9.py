salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

while months != 0:
    need_money = need_money - spend + salary
    spend = spend * increase + spend
    months -= 1

need_money = abs(need_money)
print(round(need_money))
