# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:36:41 2015

@author: Dani
"""
from sys import argv
def fasta2sec(fastafile):
    '''Lee un fasta y devuelve la secuencia que contiene'''
    F = open(fastafile)
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
if len(argv) != 3:
    print 'Usage: python ArgsCompareProt.py prot1.fasta prot2.fasta'
    exit()
    
D = fasta2sec(argv[1])
H = fasta2sec(argv[2])
counter = 0
for pos in range(min([len(H),len(D)])):
    if H[pos] == D[pos]:
        counter += 1
else: print counter*100./min([len(H),len(D)])

