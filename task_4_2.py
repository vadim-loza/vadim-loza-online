# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

tmp = mac.split(':') #преобразуем нашу строку во временный список

mac = '.'.join(tmp) #создаем нужную строку с разделителем '.'

print(mac)

#Но так как мы еще, вроде, не изучали join, то проще сделать как в предыдушем задании методом replace:

#mac = mac.replace(':', '.')
