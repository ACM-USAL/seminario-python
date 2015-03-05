# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 19:12:13 2014

@author: Dani
"""
"""
a = int(raw_input("Dame cinco valores enteros, uno a uno: "))
b = int(raw_input("Va, otro: "))
c = int(raw_input("Te quedan tres: "))
d = int(raw_input("Sólo dos más: "))
e = int(raw_input("Ya el último: "))
print sorted([a, b, c, d, e])
#Otra forma muy compacta
print sorted([int(raw_input("Dame cinco valores: ")), int(raw_input("Te quedan cuatro: ")),int(raw_input("Otros tres: ")),  int(raw_input("Dos más: ")), int(raw_input("El último: "))])
"""
#Una forma intermedia
lista = []
lista.append(int(raw_input("Dame cinco valores enteros, uno a uno: ")))
lista.append(int(raw_input("Va, otro: ")))
lista.append(int(raw_input("Te quedan tres: ")))
lista.append(int(raw_input("Sólo dos más: ")))
lista.append(int(raw_input("Ya el último: ")))
print sorted(lista)