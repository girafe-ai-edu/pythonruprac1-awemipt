# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""

num_4 = int(input("Enter 4 digit number: "))
if abs(num_4) < 1000 or abs(num_4) > 9999:
    raise Exception("you entrered not 4 digit number")
print(sum(list(str(num_4))))