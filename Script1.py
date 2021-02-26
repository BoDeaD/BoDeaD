#python
import math
while (True):
 print ("Эта прога решает квадратные уровнения\n Чтобы завершить прогу в .Введите коофицыент a - . напишите данный ключ:\n 229581")
 exemple_a = int(input('Введите коофицыент a - '))
 exemple_b = int(input('Введите коофицыент b - '))
 exemple_c = int(input('Введите коофицыент c - '))
 D = exemple_b ** 2 - 4 * exemple_a * exemple_c
 x1 = ((exemple_b * -1) + math.sqrt(D)) / (2 * exemple_a)
 x2 = ((exemple_b * -1) - math.sqrt(D)) / (2 * exemple_a)
 x3 = (exemple_b * -1) / (2 * exemple_a)
 print(f"D = b ** 2 - 4 * a * c = {exemple_b} ** 2 - 4 * {exemple_a} * {exemple_c} = {D}")
 print(f"Дискреминант(D) = {D}")
 if exemple_a == 229581:
     print("Ключ введён ВЕРНО\n Программа завершила роботу")
     break
 if D > 0:
    print(f'x1 = ((b * -1) + Корень(D)) / (2 * a) = (({exemple_b} * -1) + {math.sqrt(D)}) / (2 * {exemple_a}) = {x1}')
    print(f'x2 = ((b * -1) + Корень(D)) / (2 * a) = (({exemple_b} * -1) - {math.sqrt(D)}) / (2 * {exemple_a}) = {x2}')
 elif D == 0:
    print(f'x3 = ((b * -1) + 0 / (2 * a) = ({exemple_b} * -1) / (2 * {exemple_a}) = {x3}')
 elif D < 0:
    print("D < 0 => Нет корней")
 else:
    print("Error")
    break
'''
Программу проверял с помощью этого уровнения: 2x**2 - 3x - 9;
Если найдёте ошибки пишите на мою почту lageroped7@gmail.com
'''

