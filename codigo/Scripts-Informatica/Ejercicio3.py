# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 14:46:55 2014

@author: Dani

EJERCICIO 3: Escribir un texto dado en forma de pirámide
"""
#pedimos una palabra. Podíamos añadir condiciones si quisieramos...
texto = raw_input("Escribe una palabra: ")
#salida = '' 
n=len(texto)
#bucle for. Itera desde 0 hasta n, la longitud de la cadena
for x in range(0,n):
    print texto[0:x]
#Esto es otra forma de hacer el primer bucle, sumando caracteres a una cadena (línea 11)
"""for letra in texto:
    salida += letra
    print salida"""
#bucle for. Itera desde n hasta 0, con paso -1
for x in range(n,0,-1):
    print texto[0:x]
