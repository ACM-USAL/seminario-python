#!/usr/bin/env python3
# -*- coding: utf-8 -*-
entero = 3
real = 4.5
cadena = "Monty"
complejo = 3 + 4j
cadena_num = "4"
#Esto es ilegal
cadena_num + real

#Sin embargo, esto funciona:
entero + int(cadena_num)

#Esto también
string(entero) + cadena_num

#Para números Python es más flexible
real + complejo
