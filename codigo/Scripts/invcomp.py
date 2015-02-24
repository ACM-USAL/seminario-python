# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 22:46:43 2015

@author: Dani
"""
#Se pide una cadena
comp_dic = {'A':'T','T':'A','C':'G','G':'C'}
dna = raw_input('Escriba una cadena de DNA: ')
dna = dna.upper()
comp = ''
for nuc in dna:
    if nuc not in ['A', 'T', 'C', 'G']:
        print 'No es DNA. Revise su cadena'
        exit()
    else: comp += comp_dic[nuc]
invcomp = comp[::-1]
print 'La cadena inversa complementaria es: %s' %invcomp