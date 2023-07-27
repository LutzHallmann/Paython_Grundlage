'''
Auslesen einer Fremddatei
'''

import urllib.request as ur     # Zugriffe auf URLs

url = 'http://www.business-rules.org/files/2023KW28Python.zip'

Antwort = ur.urlopen(url)
BinaerDatei = Antwort.read()
f = open('GrundKursPython.zip','wb')
f.write(BinaerDatei)
f.close()

