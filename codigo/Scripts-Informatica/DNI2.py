# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 23:01:23 2014

@author: Dani
"""

nif = int(raw_input("Escribe el número de tu DNI: "))
resto = nif % 23
equivalencia = 'TRWAGMYFPDXBNJZSQVHLCKE'
print "Tu DNI completo es", nif, equivalencia[resto]