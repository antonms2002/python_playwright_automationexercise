import datetime

today = datetime.date.today()
print(today)

print(datetime.datetime.now())

now = datetime.datetime.now()
print(f"Текущий момент: {now}")

# Создадим интервал в 15 дней и 3 часа
delta = datetime.timedelta(days=15, hours=3)

# Узнаем, какая дата будет через этот интервал
future_date = now + delta
print(delta)
print(f"Через 15 дней и 3 часа: {future_date}")

# Аналогично можно вычесть интервал, чтобы узнать прошедшую дату
past_date = now - delta
print(f"15 дней и 3 часа назад: {past_date}")