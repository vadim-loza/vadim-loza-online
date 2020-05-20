# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

#######

tmp1 = command1.split() #Создаем список с разделителем "пробел" из первой команды

tmp2 = command2.split() # И для второй комманды

vlans1 = tmp1[-1].split(',') # Вытягиваем данные из последнего элемента, создав из них список виланов с разделителем ",".

vlans2 = tmp2[-1].split(',') # И для воторого списка виланов.

vlans = list(set(vlans1) & set(vlans2)) #Создаем два множества и их пересечение
#выводим в новый список вланов. Пробую в одну строку, но наверное рано мне.

print(vlans)
