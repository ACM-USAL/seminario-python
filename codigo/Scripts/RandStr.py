# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:29:15 2015

@author: Dani
"""

import random
from sys import argv
filename = 'string_file.txt'

DNAnucs = ['A','T','C','G']
RNAnucs = ['A','U','C','G']
AAs= ['A', 'C', 'D', 'E', 'F', 'G', 
'H', 'I', 'K', 'L', 'M', 'N', 'P', 
'Q', 'R', 'S', 'T', 'V', 'W', 'Y', '_']

def randstr(itemlist, length):
    string = ''
    for i in range(int(length)):
        string += random.choice(itemlist)
    return string
    
if len(argv) != 3:
    if len(argv) == 4:
        filename = argv[3]
    else:
        print 'Usage: python rand_create.py "type of string" "length" (=filename)'
        print 'Types of strings: /n    -dna -> DNA /n    -rna -> RNA /n    -aa -> Protein (Aminoacids)'
        exit()
F = open(filename,'w')
if argv[1] == '-dna':
    F.write(randstr(DNAnucs, argv[2]))
elif argv[1] == '-rna':
    F.write(randstr(RNAnucs, argv[2]))
elif argv[1] == '-aa':
    F.write(randstr(AAs, argv[2]))
print 'Done!'    