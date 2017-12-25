#!/usr/bin/env python

import sys

current_nucl=None
for line in sys.stdin:
    line=line.split("\t")
    antiNucleus=line[0]
    eventFile=line[1]
    prodTime=line[2]
    if current_nucl==None:	
       current_nucl=antiNucleus
       counter=0
       sum=0
       eventFiles=[]
    if current_nucl!=antiNucleus:
       print('{}\t{}\t{}'.format(antiNucleus,len(set(eventFiles)),sum/counter)) 
       current_nucl=antiNucleus
       counter=0
       sum=0
       eventFiles=[]
    eventFiles.append(eventFile)
    sum+=float(prodTime)
    counter+=1
print('{}\t{}\t{}'.format(antiNucleus,len(set(eventFiles)),sum/counter))
