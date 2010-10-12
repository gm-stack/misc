#!/usr/bin/env python
import socket,thread,commands

def interact(conn):
	a = commands.getoutput("""osascript -e 'tell application "iTunes" to get the artist of the current track' 2>/dev/null""")
	b = commands.getoutput("""osascript -e 'tell application "iTunes" to get the name of the current track' 2>/dev/null""")
	conn.send("%s - %s" % (a,b))
	conn.close()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(50)

while 1:
	conn, addr = serversocket.accept()
	thread.start_new_thread(interact,(conn,))
