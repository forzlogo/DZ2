'''Пользователь вводит номер дня недели. Выведите строĸу 'Выходные', если
введенное число равно 6 или 7. В случае, если число лежит в диапазоне от 1 до 5
вĸлючительно, выведите строĸу 'Будни'.'''

a = int(input("Введите номер для недели - "))

if a < 0 or a > 7:
    print("Ошибка")
elif a >= 1 and a <= 5:
    print("Будни")
else:
    print("Выходные")