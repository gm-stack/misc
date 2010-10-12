#!/usr/bin/env python

import random
import sys
import psyco
psyco.full()

src = [1,4,3,5,2,7,9,15,26,41,52]
dst = [1,2,3,4,5,7,9,15,26,41,52]

print len(src)
print len(dst)

i=0

while 1:
	random.shuffle(src)
	i+= 1
	if (i % 100000 == 0):
		sys.stdout.write(".")
		sys.stdout.flush()
	if src == dst:
		print src
		break

print i