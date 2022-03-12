a = float(input ("Введи сумму, поступившую на счёт: "))
d = 1.01
import math
x = math.floor(a / d)
s = x / 100
c = round((a - (x + s)), 2)
print ("Сумма для вывода: " + str(x))
print ("Банк забирает 1% от вывода: " + str(s))
print ("Остаток на счёте: " + str(c))

Различные вариации кода


a = float(input ("Введи сумму, поступившую на счёт: "))
d = 1.01
import math
from decimal import Decimal
x = math.floor(a / d)
s = x / 100
c = Decimal(a - (x + s))
c.quantize(Decimal('0.00'))
print ("Сумма для вывода: " + str(x))
print ("Банк забирает 1% от вывода: " + str(s))
print ("Остаток на счёте: " + str(c.quantize(Decimal('0.00'))))

a = float(input ("Введи сумму, поступившую на счёт: "))
d = 1.01
import math
import decimal
x = math.floor(a / d)
s = x / 100
c = decimal.Decimal(a - (x + s))
c.quantize(decimal.Decimal('0.00'))
print ("Сумма для вывода: " + str(x))
print ("Банк забирает 1% от вывода: " + str(s))
print ("Остаток на счёте: " + str(c.quantize(decimal.Decimal('0.00'))))


a = float(input ("Введи сумму, поступившую на счёт: "))
d = 1.01
print ("Сумма для вывода: " + str(a // d))
print ("Банк забирает 1% от вывода: " + str((a // d) / 100))
print ("Остаток на счёте: " + str(round((a - ((a // d) + ((a // d) / 100))), 2)))


a = float(input ("Введи сумму, поступившую на счёт: "))
d = 1.01
x = int(a / d)
print ("Сумма для вывода: " + str(x))
print ("Банк забирает 1% от вывода: " + str(x / 100))
print ("Остаток на счёте: " + str(round((a - (x + (x / 100))), 2)))


a = float(input ("Введи сумму, поступившую на счёт: "))
d = 1.01
x = a // d
print ("Сумма для вывода: " + str(x))
print ("Банк забирает 1% от вывода: " + str(x / 100))
print ("Остаток на счёте: " + str(round((a - (x + (x / 100))), 2)))
