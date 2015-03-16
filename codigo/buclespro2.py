#!/usr/bin/env python3
# -*- coding: utf-8 -*-

multiplos_siete = []
for i in range(1,200):
  if(i % 7 != 0):
    continue
  
  multiplos_siete.append(i)

#counter =1 
#for i in multiplos_siete:
#  print(i/counter) 
#  counter = counter +1

print(multiplos_siete)  
