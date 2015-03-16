#!/usr/bin/env python3
# -*- coding: utf-8 -*-


lista = [4,"8","15",16,23,42, "isla", True]

for elemento in lista:
  print(elemento)

print(lista[:-1])
print(lista[0:6:2])
print(lista[4:])

lista.reverse()

lista.sort()
lista.count()

sum(lista[:3])
lista.remove()

#TODO: morir personajes GoT
