#!/usr/bin/env python
import os,random
get,put = os.popen4("/bin/ps -ax -o pid")
text = put.read()
text = text.split("\n")
text = text[1:-1]
pid = random.choice(text)
print pid
os.system("kill -9 %s" % pid)
