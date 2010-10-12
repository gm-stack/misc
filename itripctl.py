#!/usr/bin/env python
import sys, wave
from AppKit import NSSound
from time import time

frequency = float(sys.argv[1])
if (frequency < 76.0 or frequency > 108.0):
	print "Invalid frequency"
	exit()

class sound:
    def __init__(self, file):
        self._sound = NSSound.alloc()
        self._sound.initWithContentsOfFile_byReference_(file, True)
    def play(self): self._sound.play()
    def is_playing(self): return self._sound.isPlaying()

frequency = int(frequency*10) - 752

endseq = "1001"

one = wave.open("one.wav",'r')
onedata = one.readframes(one.getnframes())
zero = wave.open("zero.wav",'r')
zerodata = zero.readframes(zero.getnframes())

out = wave.open("out.wav",'w')
out.setnchannels(2)
out.setsampwidth(2)
out.setframerate(44100)

if (len(sys.argv) > 2):
	if (sys.argv[2] == "-m"):
		endseq = "0001"

def backwards_binary_3(number):
	digit1 = str(number & 1)
	digit2 = str((number & 2) / 2)
	digit3 = str((number & 4) / 4)
	return digit1 + digit2 + digit3

def backwards_binary_4(number):
	digit1 = str(number & 1)
	digit2 = str((number & 2) / 2)
	digit3 = str((number & 4) / 4)
	digit4 = str((number & 8) / 8)
	return digit1 + digit2 + digit3 + digit4

block1 = backwards_binary_4(int(frequency % 16))
block2 = backwards_binary_4(int(((frequency + 240) % 256) / 16))
block3 = backwards_binary_3(int((frequency + 15*16) / 256) + 2)

code = "1010 %s %s %s %s" % (block1,block2,block3,endseq)
print code
time = 0.02
for char in code:
	if (char == "1"):
		out.writeframes(onedata)
	if (char == "0"):
		out.writeframes(zerodata)
outsnd = sound("out.wav")
outsnd.play()
while (outsnd.is_playing()):
	pass
