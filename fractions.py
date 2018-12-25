def cancel(a, b, c):
    d = a + b
    while c != 0:
        (d, c) = (c, d % c)
    return d


n1, d1 = map(int, input("Введите первую дробь: ").split('/'))
n2, d2 = map(int, input("Введите вторую дробь: ").split('/'))

if d1 == d2:
    print('Сумма дробей равна: {}/{}'.format((n1 + n2)//cancel(n1, n2, d1), d1//cancel(n1, n2, d1)))
    print('Разность дробей равна: {}/{}'.format((n1 - n2)//cancel(n1, -n2, d1), d1//cancel(n1, -n2, d1)))

else:
    num1 = n1 * d2
    num2 = n2 * d1
    denom = d1 * d2
    print('Сумма дробей равна: {}/{}'.format((num1 + num2)//cancel(num1, num2, denom), denom//cancel(num1, -num2, denom)))
    print('Разность дробей равна: {}/{}'.format((num1 - num2)//cancel(num1, -num2, denom), denom//cancel(num1, -num2, denom)))
