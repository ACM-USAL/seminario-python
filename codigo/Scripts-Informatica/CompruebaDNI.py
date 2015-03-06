# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 19:20:45 2014

@author: Dani
"""

dni = raw_input('Escribe tu dni: ')
letra = dni[-1].upper()
numero = int(dni[0:-1])
resto = numero % 23
equivalencia = 'TRWAGMYFPDXBNJZSQVHLCKE'
if equivalencia[resto] == letra:
    print "Perfecto, has introducido bien el dni"
else: 
    print "O te has confundido o me intentas fular"
    print "Repite anda..."
