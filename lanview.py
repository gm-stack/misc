#!/usr/bin/env python
import cPickle, httplib
hostname = "authenticator.streetgeek.lan"

def whatis_ip(conn,ipnum):
	conn.putrequest('GET', "/api/httpget/pickle/whatis_ip/?ip=%s" % ipnum)
	conn.endheaders()
	response = conn.getresponse()
	print "whatis"
	return cPickle.loads(response.read())

def whois_ip(conn,ipnum):
	conn.putrequest('GET', "/api/httpget/pickle/whois_ip/?ip=%s" % ipnum)
	conn.endheaders()
	response = conn.getresponse()
	print "whois"
	return cPickle.loads(response.read())

def icon(type):
	return "https://authenticator.streetgeek.lan/media/console_icons/%s.png" % type
	
def htmlify(conn,ipnum):
	print "getting data for %s" % ipnum
	whois = whois_ip(conn,ipnum)
	if (type(whois) is bool):
		return """<td id="empty"><center><br><br>%s</center></td>""" % ipnum
	interneton = ""
	if not (whois['internet_on']):
		interneton = ' id="nointernet"'
	whatis = whatis_ip(conn,ipnum)
	stret = """<td%s><center><img src="%s"><br>
	%s<br>
	%s<br>
	%s<br>
	%s<br></center>
	</td>""" % (interneton,icon(whatis['type']),whatis['ip_address'],whatis['mac_address'],whatis['computer_name'].replace(".streetgeek.lan",""),whois['username'])
	return stret

conn = httplib.HTTPSConnection(hostname)
f = open("output.htm","w")
f.write("""<html><head>
<title>LanView 0.1</title>
<style type="text/css">
<!--
table {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 9px;
	border-top-style: none;
	border-right-style: none;
	border-bottom-style: none;
	border-left-style: none;
}
td {
	border: thin dashed #999999;
	background-color: #EEEEEE;
	width: 12.5%;
	height: 54pt;
}
#empty {
	background-color: #293F5A;
	border-top-style: none;
	border-right-style: none;
	border-bottom-style: none;
	border-left-style: none;
	color: #999999;
	border-top-width: thin;
	border-right-width: thin;
	border-bottom-width: thin;
	border-left-width: thin;
}
body {
	background-color: #3F6089;
}
#nointernet {
	background-color: #999999;
}
-->
</style>
</head><body>
<table width="100%" border="1">
<tr>
""")
iplist = []
for i in [0,1]:
	for j in range(0,255):
		iplist += ["10.4.%i.%i" % (i,j)]
count = -1
for i in iplist:
	count += 1
	if ((count % 8) == 0):
		f.write("</tr><tr>")
	f.write(htmlify(conn,i))
	f.flush()

f.write("</tr></table>")
	