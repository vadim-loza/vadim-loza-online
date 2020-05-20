# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#######

table_list = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbond Interface:'] #Создаем список для последующего использования в таблице.

ospf_route = ospf_route.split() #Преобразуем строку в список без лишних пробелов
ospf_route.remove('via') #Удаляем лишний элемент
ospf_route[0] = 'OSPF' #Меняем сокращенное значение на более полное.
print( 
    '\n'+'{:22} {:22}'.format(table_list[0], ospf_route[0]), 
    '\n'+'{:22} {:22}'.format(table_list[1], ospf_route[1]),
    '\n'+'{:22} {:22}'.format(table_list[2], ospf_route[2]),
    '\n'+'{:22} {:22}'.format(table_list[3], ospf_route[3]),
    '\n'+'{:22} {:22}'.format(table_list[4], ospf_route[4]),
    '\n'+'{:22} {:22}'.format(table_list[5], ospf_route[5])
    )
# Выводим результат на экран.
# P.S. Понимаю, что задание можно выполнить намного элегантнее и проще, по пока так. )) Спасибо.
