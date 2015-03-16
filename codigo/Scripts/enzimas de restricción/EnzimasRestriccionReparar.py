# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 18:42:52 2014

@author: Dani
"""

# -*- coding: utf-8 -*-
import re

def fasta2sec (fastafile) :
  """ Lee un fichero FASTA y
  devuelve la secuencia que contiene """
  F = open (fastafile)
  secuencia = ""
  for linea in F :
    linea = linea.strip("\n")
    if len(linea) != 0 and linea[0] != '>':
      secuencia = secuencia + linea
  return secuencia

def iupac2regex (iupac) :
  i2r = { 'A':'A', 'C':'C', 'G':'G', 'T':'T',
          'R':'[GA]', 'Y':'[CT]', 'M':'[AC]', 'K':'[GT]' ,
          'S':'[GC]', 'W':'[AT]', 'B':'[CGT]', 'D':'[AGT]',
          'H':'[ACT]', 'V':'[ACG]', 'N':'[ACGT]'}
  return i2r[iupac]

def bionet2dict (bionet_file) :
  enzima_regex={}
  enzima_iupac={}
  file = open(bionet_file)
  p=re.compile(r'(\w+) (\((\w+)\))?\s+(\w*\^*\w*)')
  flag = 0
  for linea in file:
    #print linea
    if flag :
      m = p.search(linea)
      if m :
        nombre=m.group(1)
        alias=m.group(3)
        iupac_exp =m.group(4)
        enzima_iupac[nombre] = iupac_exp # diccionario
        iupac_exp = iupac_exp.replace('^','')
        reg_exp = "" # expresión regular
        for c in iupac_exp:
          reg_exp += iupac2regex(c)
        
        if nombre not in enzima_regex.keys():
            enzima_regex[nombre]=reg_exp # diccionario
            enzima_regex[alias]=reg_exp
        else:
            enzima_regex[nombre].append(reg_exp)
            enzima_regex[alias].append(reg_exp)
            
      continue
    if re.match(r'Rich Roberts', linea) :
      flag = 1
      continue
  return enzima_iupac, enzima_regex

### PROGRAMA PRINCIPAL
chrIII = fasta2sec("SPIII.fasta")
(enzima_iupac,enzima_regex)=bionet2dict('bionetc.txt')
#for enzima in enzima_regex.keys() :
#  print enzima, enzima_regex[enzima]

while True:
  entrada = raw_input("Dame el nombre de un enzima de restricción: ")
  if entrada == "fin" :
    print "Gracias por utilizar este programa"
    exit()
  if entrada not in enzima_regex.keys() :
    print "El nombre del enzima no existe, inténtelo con otro"
    continue
  else :
    for i in enzima_regex[entrada]:
        #p = re.compile(enzima_regex[entrada])
        print entrada, i
        m = re.finditer(i,chrIII)
        if m :
          for i in m :
            print "Encontrado %s en %d-%d " % (i.group(), i.start(), i.end() )