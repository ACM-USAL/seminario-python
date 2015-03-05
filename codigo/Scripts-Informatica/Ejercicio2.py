# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 17:47:35 2014

@author: Dani

EJERCICIO 2: Pide una frase y escribe sólo las iniciales y en mayúscula
"""
#pedimos una frase y la almacenamos
frase = raw_input("Escribe una frase: ")
#extraemos los elementos (palabras) de la frase, separadas por un espacio (' ')
palabras = frase.split(' ')
#definimos una lista donde almacenaremos las iniciales
resultado = []
#bucle for
for objeto in palabras:
    #Añadimos a la lista "resultado" el primer caracter(0) en mayúsculas...
    #...de cada elemento iterado (objeto) de la lista "palabras"
    resultado.append(objeto[0].upper())
#print de una cadena con los elementos de "resultado"... 
#...unidos por una string vacía (juntas)
print ''.join(resultado)


"""
Alternativa más simple 

resultado = ''
for objeto in palabras:
    resultado += objeto.upper()
"""