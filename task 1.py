salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

def calculate_safety_capital(salary, spend, increase, months):
    current_spend = spend
    money_capital = 0

    for month in range(months):
        deficit = max(0, current_spend - salary)
        money_capital += deficit
        current_spend *= (1 + increase)

    return round(money_capital)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
required_money_capital = calculate_safety_capital(salary, spend, increase, months)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_money_capital, end="\n")
