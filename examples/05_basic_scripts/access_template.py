#!/usr/bin/env python3

###
Сначала элементы списка объединяются в строку, которая разделена символом \n, а в строку
подставляется номер VLAN, используя форматирование строк.
###

access_template = ['switchport mode access',
                  'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                  'spanning-tree bpduguard enable']

print('\n'.join(access_template).format(5))
