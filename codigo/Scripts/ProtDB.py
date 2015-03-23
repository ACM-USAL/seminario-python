# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:41:55 2015

@author: Dani
"""
import urllib2, re, webbrowser
F = ''
while not F:
    standard_url_rcbs = 'http://www.PDB.org/pdb/explore.do?structureId='
    add_url = raw_input('Insert valid RCSB protein code: ').upper()
    if add_url == 'FIN':
        print 'Bye bye'
        exit()
    type(add_url)
    final_url =standard_url_rcbs + add_url
    F = urllib2.urlopen(final_url)
db = 10
error_count = 0
while error_count < 3 and (db > 4 or db < 1):
    db = int(raw_input('Choose a database number [PDB(1), PDB structure UniProt(3), UniProt fasta(4)]: '))
    if db == 1:
        webbrowser.open(final_url)
        break
    elif db == 2:
        webbrowser.open('http://www.rcsb.org/pdb/explore/jmol.do?structureId=' + add_url)
        break
    elif db == 3 or db == 4:    
        for line in F:
            url = re.search('href=\"(http://www\.uniprot\.org/uniprot/.+?)\"',F.read())
            if url:
                if db == 3:
                    print url.group(1)
                    webbrowser.open(url.group(1))
                elif db == 4:
                    print url.group(1) + '.fasta'
                    webbrowser.open(url.group(1) + '.fasta')
                break
            else: 
                print "Script isn't working. Sorry for the inconvenience"
                exit()
        break
    else: error_count += 1
    print error_count
else: 
    if error_count >= 3: 
        print 'User not responding, exiting...'
        exit()
print 'Thank you for using.'