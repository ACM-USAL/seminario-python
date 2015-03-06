# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 19:41:15 2014

@author: Dani

EJERCICIO 5: Pedir un entero y escribir el factorial de todos los enteros hasta ese.
"""
#Pedimos el número
numero = int(raw_input("Dime un entero: "))
#definimos la variable factorial, para poder usarla después en la operación
factorial = 1
#Iteramos del 1 al número dado
for x in range(1,numero+1):
    #redefinimos la variable factorial con factorial por el valor actual de la iteración
    #(es una operación acumulativa)
    factorial *= x
    #imprimimos con formato para que quede bonito
    print 'El factorial de %3d es: %10d' %(x,factorial)