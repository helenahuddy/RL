#!/usr/bin/env python
import sys

with open('out1.txt', 'r') as f:
    read_data = f.read()
av_prodTimes={}
for line in read_data:
    antiNucleus, av_prodTime = line.split('\t')
    av_prodTimes[antiNucleus]=av_prodTime

for line in sys.stdin:
    antiNucleus = int(line[0])
    eventFile = line[1]
    prodTime = line[10]
    if float(prodTime)>float(av_prodTimes[antiNucleus]):
    	print('{}\t{},{}'.format(antiNucleus,eventFile,prodTime))
