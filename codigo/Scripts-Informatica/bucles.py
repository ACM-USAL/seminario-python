#!/usr/bin/env python3
lista = []
cadena = input("Dame una cadena!\n")
while cadena != "":
	lista.append(cadena)
	cadena = input("Dame una cadena!\n")
else:
	for elemento in lista:
		print(elemento)

lista = range(0,20)
suma = 0
for elemento in lista:
	if elemento % 2 == 0:
		continue
	else:
		suma += elemento

print(suma)

lista = []

while True:
	cadena = input("Dame una cadena!\n")
	if cadena == "":
		break
	lista.append(cadena)

lista.sort()
print(lista)

