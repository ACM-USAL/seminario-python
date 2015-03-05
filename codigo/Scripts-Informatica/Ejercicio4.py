# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 19:32:47 2014

@author: Dani

EJERCICIO4: Escribir las fichas de dominó
"""
#Bucle for, itera y da valores a x desde 0 hasta 6
for x in range(0,7):
    #Bucle for, para cada valor de x asigna valores a y desde x hasta 6
    for y in range(x,7):
        #Escribe en la forma 'x:y'
        print "%s:%s" %(x,y)
  