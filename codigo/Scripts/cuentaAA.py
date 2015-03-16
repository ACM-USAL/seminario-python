# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 19:15:49 2014

@author: Dani
"""

file = open (raw_input('Escribe la ruta de tu fichero: '))
secuencia = ''
#Iniciamos el bucle de lectura
for linea in file:
    #Asociamos a la variable "linea" cada línea del archivo, pero sin el salto de línea
    linea = linea.strip('\n')
    #Comprobamos que la línea no está vacía, ni empieza por '>' (1ª linea de info)
    if linea != '' and linea[0] != '>' :
        #Añadimos a la variable "secuencia" cada iteración de linea
      secuencia = secuencia + linea
print 'Tu proteína tiene %d aminoácidos' %len(secuencia)
#Definimos las listas con los datos que queremos y sus resp. contadores
hydrophilic = ['C', 'F', 'I', 'L', 'M', 'V', 'W']
count_hphi=0
hydrophobic = ['D', 'E', 'G', 'K', 'N', 'P', 'Q', 'R', 'S', 'T']
count_hpho=0
neutral = ['A', 'H', 'Y']
count_neu=0
#Iteramos la secuencia por elemento
for aa in secuencia:
    #Comprobamos dónde está cada aa, y sumamos 1 al contador correspondiente a su tipo
    if aa in hydrophilic:
        count_hphi += 1
    elif aa in hydrophobic:
        count_hpho += 1
    elif aa in neutral:
        count_neu += 1
    #Añadimos "else" por si acaso
    else: 
        print 'Algún dato no es AA. Revisa el fichero'
        #Preguntamos si el usuario quiere continuar
        pregunta = raw_input('¿Quieres continuar de todos modos? [s/n]')
        #Si la respuesta es sí...
        if pregunta == 'y' or pregunta == 'Y':
            continue
        #Si la respuesta es no...
        elif pregunta =='n' or pregunta == 'N':
            exit()
        #Si la respuesta es otra...
        else: exit()
#Imprimimos la respuesta con los datos
print 'La cantidad de aa de cada tipo es: '
print '%.2f %% de hidrofílicos' %(float(count_hphi)/len(secuencia)*100)
print '%.2f %% de hidrofóbicos' %(float(count_hpho)/len(secuencia)*100)
print '%.2f %% de neutros' %(float(count_neu)/len(secuencia)*100)
