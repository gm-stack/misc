#!/usr/bin/env python
import os,sys,time

try:
	interface = sys.argv[1]
except:
	interface = "ppp0" #default

strlength = 0

while (1):
	put,get = os.popen2("netstat -I %s -b" % interface)
	output = get.read()
	output = output.split("\n")[-2]
	if not output.count(interface):
		print "No such interface " + interface
		sys.exit()
	
	while (output.find("  ") != -1):
		output = output.replace("  "," ")
	output = output.split(" ")
	
	interface = output[0]
	ip = output[3]
	ibytes = float(output[6])
	obytes = float(output[9])
	iMB = ibytes/1048576
	oMB = obytes/1048576
	
	strprint =  "Data usage for interface %s : %.2fMB in, %.2fMB out = %.2fMB total" % (interface, iMB, oMB, iMB+oMB )
	sys.stdout.write("\b" * strlength)
	strlength = len(strprint)
	sys.stdout.write(strprint)
	sys.stdout.flush()
	
	time.sleep(1)
