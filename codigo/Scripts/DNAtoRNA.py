# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 18:46:48 2014

@author: Dani
"""

dna=raw_input("¿Cómo es tu DNA?")
dna=dna.upper()
rna=dna.replace('T', 'U')
print 'Tu RNA es: %s ' %rna
#otra forma simplificada:
print'Tu RNA es: %s ' %((raw_input("¿Cómo es tu DNA?")).upper()).replace('T', 'U')