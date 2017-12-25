#!/usr/bin/env python
import sys
for line in sys.stdin:
    line=line.split(',')
    antiNucleus=line[0]
    prodTime=line[10]
    print('{}\t{}'.format(antiNucleus,prodTime))



# bigdata
