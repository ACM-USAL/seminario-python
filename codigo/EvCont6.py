# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 18:17:55 2014

@author: Dani
"""

# Codigo genetico
gencode = {
  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
  'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
  'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
  'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
  'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
  'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
  'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
  'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
  'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
  'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
  'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
  'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
  'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
  'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
  'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
  'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# Lista de aminoacidos
aminoacidos = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 
               'I', 'K', 'L', 'M', 'N', 'P', 'Q',  
               'R', 'S', 'T', 'V', 'W', 'Y', '_']
               
# Diccionario que para cada aminoacido
# da como valor la lista de codones que lo codifican
# separados por el caracter ":"
aa2codon={'A':'GCA:GCC:GCG:GCT', 'C':'TGT:TGC', 'D':'GAT:GAC', 
          'E':'GAG:GAA', 'F':'TTT:TTC', 'G':'GGT:GGG:GGA:GGC' , 
          'H':'CAT:CAC', 'I':'ATC:ATA:ATT', 'K':'AAG:AAA', 
          'L':'CTC:CTG:CTA:CTT:TTA:TTG', 'M':'ATG', 'N':'AAC:AAT', 
          'P':'CCT:CCG:CCA:CCC', 'Q':'CAA:CAG', 
          'R':'AGG:AGA:CGA:CGC:CGG:CGT', 
          'S':'AGC:AGT:TCG:TCA:TCC:TCT', 
          'T':'ACC:ACA:ACG:ACT', 'V':'GTA:GTC:GTG:GTT',
          'W':'TGG', 'Y':'TAT:TAC', '_':'TAG:TAA:TGA'}
          
#Abrimos el archivo (en este caso pidiendo el path)
#file = open(raw_input('Escribe la ruta de tu fasta: ')
file = open('SP.fasta')
#Definimos la variable "secuencia"
secuencia = ''
#Iniciamos el bucle de lectura
for linea in file:
    #Asociamos a la variable "linea" cada línea del archivo, pero sin el salto de línea
    linea = linea.strip('\n')
    #Comprobamos que la línea no está vacía, ni empieza por '>' (1ª linea de info)
    if linea != '' and linea[0] != '>' :
        #Añadimos a la variable "secuencia" cada iteración de linea
      secuencia = secuencia + linea
#Añadimos la función que queramos, ya tenemos la secuencia almacenada en "secuencia"
#file = open(raw_input('Escribe la ruta de tu archivo de exones: '))
file = open('CDScoords.txt')

#Alternativa para customizar el programa. Esto lee el nombre del primer gen en
#vez de que se lo demos en el código
'''for linea in file:
    pos = linea.split()
    a = pos[0]
    break'''
a = 'SPAC212.06c'
nueva_secuencia = ''
for linea in file:
    pos = linea.split()
    if pos[0] == a:
        nueva_secuencia += secuencia[int(pos[1])-1:int(pos[2])]
    else:
        print 'Para el gen %s: ' %a #Y ahora la función que hace todo
        codon_counter={'A':[0,0,0,0], 'C':[0,0], 'D':[0,0], 
          'E':[0,0], 'F':[0,0], 'G':[0,0,0,0] , 
          'H':[0,0], 'I':[0,0,0], 'K':[0,0], 
          'L':[0,0,0,0,0,0], 'M':[0], 'N':[0,0], 
          'P':[0,0,0,0], 'Q':[0,0], 
          'R':[0,0,0,0,0,0], 
          'S':[0,0,0,0,0,0], 
          'T':[0,0,0,0], 'V':[0,0,0,0],
          'W':[0], 'Y':[0,0], '_':[0,0,0]}
        #print nueva_secuencia
        for i in range(0,len(nueva_secuencia),3) :
            codon = nueva_secuencia[i:i+3]
            aa = gencode[codon]
            posibles_codones = aa2codon[aa].split(':')
            #print posibles_codones
            for x in range(0,len(posibles_codones)):
                #print aa, codon, x
                if codon == posibles_codones[x]:
                    codon_counter[aa][x] += 1
                    break
        #print codon_counter
        for y in aminoacidos:
            print 'Aminoácido: %s' %y
            for z in range(0,len(aa2codon[y].split(':'))):
                total = 0
                for i in codon_counter[y]:
                    total += i
                #print total
                if total == 0:
                    print '  %s %.2f%%' %(aa2codon[y].split(':')[z],(codon_counter[y][z]))
                else: print '  %s %.2f%%' %(aa2codon[y].split(':')[z],(codon_counter[y][z]*100./total))
                #print '  %s %s' %(codon_actual,porcentaje)
        nueva_secuencia = secuencia[int(pos[1])-1:int(pos[2])]
        a = pos[0]
    

    
    
    
