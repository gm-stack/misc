#!/usr/bin/env python

import os,random,time

line = "[[rate 150]] [[nmbr LTRL]] %i [[slnc 120]] %i [[slnc 120]] %i [[slnc 120]] %i [[slnc 120]] [[emph +]] [[pbas +5]]%i[[pbas -5]] [[slnc 240]]"

while True:
	say = line % (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))
	os.system("say '%s'" % say)
