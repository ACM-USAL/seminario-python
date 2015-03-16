# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 13:01:40 2014

@author: Dani
"""
#Pedimos un número para introducir por teclado
x = int(raw_input("Dime un número: "))
#Iniciamos bucle "for", que define la var divisor
#La función range nos permite iterar todos los
#números entre el uno y x (x+1 xq el interv. es abierto )
for divisor in range(1, x+1):
#Condicional dentro del bucle.
#Un nº es divisor de otro si la división tiene resto=0
    if (x % divisor) == 0:
#Imprimimos la variable definida
        print divisor