# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 19:34:10 2014

@author: Dani
"""

def fasta2sec(fastafile):
    '''Lee un fasta y devuelve la secuencia que contiene'''
    F = file (fastafile)
    #Definimos la variable "secuencia"
    secuencia = ''
    #Iniciamos el bucle de lectura
    for linea in F:
        #Asociamos a la variable "linea" cada línea del archivo, pero sin el salto de línea
        linea = linea.strip('\n')
        #Comprobamos que la línea no está vacía, ni empieza por '>' (1ª linea de info)
        if linea != '' and linea[0] != '>' :
            #Añadimos a la variable "secuencia" cada iteración de linea
            secuencia = secuencia + linea
    return secuencia
    
def identidad(sec1, sec2):
    count = 0
    for i in range(len(sec1)):
        if sec1[i] == sec2[i]:
            count += 1
        else: print i, sec1[i], sec2[i]
    return count*100./len(sec1)
    
pan = fasta2sec('pan.fasta')
sapiens = fasta2sec('sapiens.fasta')

pan = pan[216-1:659]
sapiens = sapiens[196-1:639]

print pan[0:3]
print sapiens[0:3]
    
print identidad(pan,sapiens)
