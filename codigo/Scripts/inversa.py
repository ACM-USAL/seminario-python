# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:46:43 2015

@author: Dani
"""
#Se pide una cadena
dna = raw_input('Escriba una cadena de DNA: ')
dna = dna.upper()
for nuc in dna:
    if nuc not in ['A', 'T', 'C', 'G']:
        print 'No es DNA. Revise su cadena'
        exit()
inversa = dna[::-1]

print 'La cadena inversa es: %s' %inversa