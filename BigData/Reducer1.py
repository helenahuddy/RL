#!/usr/bin/env python
import sys

current_nucl=None
for line in sys.stdin:
    line=line.split('\t')
    antiNucleus=line[0]
    prodTime=line[1]
    if current_nucl==None:	
       current_nucl=antiNucleus
       counter=0
       sum=0
    if current_nucl!=antiNucleus:
       print('{}\t{}'.format(antiNucleus,sum/counter))
       current_nucl=antiNucleus
       counter=0
       sum=0
    sum+=float(prodTime)
    counter+=1
print('{}\t{}'.format(antiNucleus,sum/counter))
