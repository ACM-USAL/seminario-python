# -*- coding: utf-8 -*-

import re

def fasta2sec(fichero):
   f = open(fichero)
   sec = ''
   for linea in f:
       linea = linea.strip('\n')
       if len(linea) != 0 and linea[0] != '>':
           sec += linea
   return sec
   
def enzimas(fichero):
    f = open(fichero)
    flag = 0
    #dicc_iupac = {}
    dicc_reg = {}
    for linea in f:
        #m = re.search(r'(\w+)\s(\((\w+)\))?\s+(\w*\^*\w*)', linea)
        if flag:
            m = re.search(r'(\w+)\s(\((\w+)\))?\s+(\w*\^*\w*)', linea)
            if m:
                nombre = m.group(1)
                #nombre2 = m.group(3)
                sec = m.group(4)
                sec = sec.replace('^', '')
                i2r = { 'A':'A', 'C':'C', 'G':'G', 'T':'T',
                       'R':'[GA]', 'Y':'[CT]', 'M':'[AC]', 'K':'[GT]' ,
                        'S':'[GC]', 'W':'[AT]', 'B':'[CGT]', 'D':'[AGT]',
                          'H':'[ACT]', 'V':'[ACG]', 'N':'[ACGT]'}
                sec2 = ''
                for i in sec:
                    regex = i2r[i]
                    sec2 += regex
                    sec2 = sec2.replace('[', '')
                    sec2 = sec2.replace(']', '')
                if nombre not in dicc_reg.keys():
                    dicc_reg[nombre] = sec2
                elif nombre in dicc_reg.keys():
                    #print 'Repetido'
                    dicc_reg[nombre] += ':' + sec2
        if re.match(r'Rich Roberts', linea):
            flag = 1
    return dicc_reg
   
dna = fasta2sec('SPIII.fasta')
#print dnaABH
dicc = enzimas('link_bionetc.txt')
#print dicc

while True:
    enz = raw_input('Introduzca el nombre de una enzima: ')
    if enz == 'fin':
        print 'Gracias por utilizar el programa'
        exit()
    elif enz not in dicc.keys():
        print 'Enzima incorrecta'
        continue
    else:
        seqs = dicc[enz].split(':')
        for seq in seqs:
            print enz, seq
            n = re.finditer(seq, dna)
            for i in n:
                print 'Encontrado %s entre las posiciones %d - %d' % (i.group(0), i.start(0), i.end(0))


        
