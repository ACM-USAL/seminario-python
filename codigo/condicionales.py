#!/usr/bin/env python3
# -*- coding: utf-8 -*-

variable = 4
print("Introduce un valor")
valor = input()
valor = int(valor)

if valor < variable:
  print("El número es menor que "+str(variable))

elif valor > variable:
  print("El número es mayor que "+str(variable))

else:
  print("El número es igual a "+str(variable))
