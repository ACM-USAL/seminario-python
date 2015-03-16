#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numero_total = 0
numero = 0
while(numero >= 0):
  numero = int(input("Introduce un número: "))
  if numero > 100:
    print("El número es muy grande. Prueba de nuevo")
    continue
  
#  if numero < 0:
#    print("Saliendo")
#    break

  numero_total += numero

else:
  print(numero_total)
