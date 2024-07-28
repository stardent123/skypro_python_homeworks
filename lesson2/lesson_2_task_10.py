def bank(X, Y):
    deposit = X
    interest_rate = 0.10

    for _ in range(Y):
        deposit += deposit * interest_rate
    return deposit

# Пример использования функции
X = 1000  # Размер вклада в рублях
Y = 5  # Срок вклада в годах
result = bank(X, Y)
print(f"Сумма на счету пользователя спустя {Y} лет: {result:.2f} рублей")
