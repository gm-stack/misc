#!/usr/bin/env python
import sys,httplib
lookup = "%20".join(sys.argv[1:])

headers = {"Accept-Encoding":"text/plain",}
conn = httplib.HTTPConnection("maps.google.com")
url = "/maps?f=q&hl=en&geocode=&q=" + lookup + "&ie=UTF8&ll=-34.923238,138.599739&spn=0.069671,0.11673&z=13&iwloc=addr&om=1&output=kml"
#print url
conn.request("GET", url, "", headers)
reply = conn.getresponse()
data = reply.read()
#print data

data1 = data.split("<name>")
data1 = data1[1].split("</name>")[0]

data2 = data.split("<coordinates>")
data2 = data2[1].split("</coordinates>")[0]
data2 = ",".join(data2.split(",")[0:2])

print "%s is at %s" % (data1,data2)