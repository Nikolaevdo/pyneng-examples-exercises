#!/usr/bin/env python3

###
#Этот скрипт позволяет в качестве аргумента параметризировать выполение скрипта.
#python access_template_argv.py Gi0/7 4
#где Gi0/7 конкретный порт, а 4 номер VLAN'a
###

from sys import argv

interface = argv[1]

vlan = argv[2]

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']


print('interface {}'.format(interface))

print('\n'.join(access_template).format(vlan))

