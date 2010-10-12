#!/usr/bin/env python
# Geordie Millar 2007
# xplane.py - a bridge between XPlane and Google Earth, using X-Plane's UDP data out and Google Earth's network link.

import time
import socket
import string
import sys
import thread

try:
	import block
except:
	print "You need PyBlock: http://members.dsl-only.net/~daniels/Block.html, please install it and run again"
	sys.exit()

port = 49000 # default, change if changed in X-Plane

svrsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
svrsocket.bind(('', port))

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print 'Set X-Plane to output data to %s port %s: ' % (ip,port)

global lat
global lon
global alt

lat = 0.0
lon = 0.0
alt = 0.0

def recvpacket(svrsocket):
	global lat
	global lon
	global alt
	while 1:
		data, address = svrsocket.recvfrom(2100)
		b = block.Block(data[10:14]) # lat
		lat = block.Readview('f',b)[0]
		b = block.Block(data[14:18]) # lon
		lon = block.Readview('f',b)[0]
		b = block.Block(data[22:26]) # ftagl
		alt = block.Readview('f',b)[0]

def outputKML(kmlname):
	f = open(("/tmp/" + kmlname), 'w') # change that for "that other operating system"
	f.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
<Document>
	<name>%s</name>
	<Style id="default+icon=http://maps.google.com/mapfiles/kml/pal3/icon63.png">
		<IconStyle>
			<Icon>
				<href>http://maps.google.com/mapfiles/kml/pal3/icon63.png</href>
			</Icon>
		</IconStyle>
	</Style>
	<Placemark>
		<name>Current Position</name>
		<styleUrl>#default+icon=http://maps.google.com/mapfiles/kml/pal3/icon63.png</styleUrl>
		<Point>
			<coordinates>%f,%f,0</coordinates>
		</Point>
	</Placemark>
	</Document>
</kml>"""% (kmlname,lon,lat))


def printlatlonalt():
	prevlen = 0
	while 1:
		time.sleep(0.25)
		sys.stdout.write("\b" * prevlen) # will another terminal app like that?
		toprint = "Latitude: %f, Longitude %f, Altitude %f" % (lat,lon,alt)
		prevlen = len(toprint)
		sys.stdout.write(toprint)
		sys.stdout.flush()
		outputKML("xplane.kml")

thread.start_new_thread(recvpacket,(svrsocket,))
thread.start_new_thread(printlatlonalt,())

while 1:
	time.sleep(1337) # keep main thread waiting