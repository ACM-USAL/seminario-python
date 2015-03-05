# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 19:41:51 2014

@author: Dani
"""
valores = int(raw_input('¿Cuantos números vas a darme? '))
lista = []
for x in range(1, valores+1):
    lista.append(float(raw_input('Número %s: ' %x)))
print lista
maximo = lista[0]
for numero in lista[1:-1]:
    if numero>maximo:
        maximo = numero
print '%s es el número más grande de los que me has dado' %maximo
        
        