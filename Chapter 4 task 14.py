# Новая задача глава 4, задача 14, c цикла for:

#1  Выведите на экран числа от 25 до 50
#2  Выведите на экран только четные числа из диапазона от 25 до 50 
#3  Выведите на экран все нечетные числа от 25 до 50, кроме техС что больше 45, с помощью дерективы continue

a=50                    # вывод до какого цифра
for i in range(24,a):   # сам цикл for, начало с 24, чтобы подсчет начался с 25
    i+=1                # цикл добавляет +1 к числу
    if i %2==0:         # условие для определения четного числа 
        if i>45:        # условия для выхода из итерации
            continue    # выход из итерации по условию
        print(i)        # Вывод сообщений на экран