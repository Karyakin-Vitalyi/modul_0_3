# 1st program
print(pow(9, 0.5) * 5)  # Возведение числа 9 в степень 0.5, затем умножение на 5

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1) #  9.99 больше 9.98 и 1000 не равно 1000.1 одновременно

# 3rd program
print(2 * 2 + 2) # Вычисление без приоритета
print(2 * (2 + 2)) # Вычисление с приоритетом для сложения
print((2 * 2 + 2) == (2 * (2 + 2))) # Сравнение результатов

# 4th program
number = float('123.456') # Преобразуем строку в дробное число
number_shifted = number * 10 # Умножаем на 10, чтобы сместить 4 в целую часть
whole_part = int(number_shifted) # Получаем целую часть числа
decimal_part = whole_part % 10 # Получаем остаток от деления на 10
print(decimal_part) # Выводим результат