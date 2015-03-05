# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 12:58:12 2014

@author: Dani

EJERCICIO 1: Escribir todas las potencias de 2 menores que 10000
"""
#definimos la variable donde se almacenará el resultado  
potencia = 1
#definimos la variable que almacenará el exponente
x=1
#Bucle while: ejecuta sentencias mientras se cumpla que potencia < 10000
while potencia < 10000:
    #print con formato
    print '%04d' %potencia
    #calcula la potencia
    potencia = 2**x
    #sube el exponente para el siguiente cálculo
    x += 1 
#el bucle termina
print 'Ya no hay más potencias de 2 menores que 10000'
#se calcula 2^13 y se almacena en "potencia". Como es mayor que 10000...
#...ya no se ejecuta el bucle while, pero el programa ha hecho el cálculo 
print '(La siguiente es %s)' %potencia


"""Segunda opción"""

#definimos la variable donde se almacenará el resultado  
potencia = 1
#definimos la variable que almacenará el exponente (esta vez cero)
x=0
#Bucle while: ejecuta sentencias mientras se cumpla que potencia < 10000
while potencia < 10000:
    #print con formato
    print '%04d' %potencia
    #sube el exponente PERO JUSTO ANTES DEL CÁLCULO
    x += 1 
    #calcula la potencia
    potencia = 2**x
    #el bucle termina
print 'Ya no hay más potencias de 2 menores que 10000'
#se calcula 2^13 y se almacena en "potencia". Como es mayor que 10000...
#...ya no se ejecuta el bucle while, pero el programa ha hecho el cálculo 
print '(La siguiente es %s)' %potencia









