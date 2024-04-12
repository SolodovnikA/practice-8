num = input('Введите число: ')
cor = 0

while num.isdigit() == False:
    num = input('Ошибка. Попробуйте еще раз. Введите число: ')
    cor = num
    if type(num) == int:
        print('Введено целое число:', cor)
        break
