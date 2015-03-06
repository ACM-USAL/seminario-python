# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 18:30:50 2014

@author: Dani
"""

numero = int(raw_input('Escribe un número para hacer su factorial: '))
factorial = 1
for x in range(1, numero+1):
    factorial = factorial*x
print "Pues este es el factorial de %s: %s" %(numero, factorial)