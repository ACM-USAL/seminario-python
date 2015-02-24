# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 13:50:53 2014

@author: Dani
"""
import re
#Hacer customizable
seqs=['AAAAAAATAAAAAAATATTTAAAAAATAAAAAAATAAAAATATAAAAAT', 'AAT']
#Cambiamos la regex para aceptar overlapping
regexp = re.compile('(?=('+seqs[1]+'))')
matches = regexp.finditer(seqs[0])
positions = ''
for pos in matches:
    positions += '%s ' %str(int(pos.start())+1)
else: positions = positions[0:len(positions)-1]
if positions:
    print 'Encontrado motivo en la(s) posicion(es):'
    print positions