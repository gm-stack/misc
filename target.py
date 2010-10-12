#!/usr/bin/env python
import sys

target = sys.argv[1]
#musthave = sys.argv[2]



def checkword(word,letters,musthave):
	for letter in word:
		if not letters.count(letter):
			return 0
	for thisletter in "abcdefghijklmnopqrstuvwxyz":
		counta = letters.count(thisletter)
		countb = word.count(thisletter)
		if (countb == counta):
			return 0
	return 1

f = open("/usr/share/dict/words",'r')
words = f.read()
words = words.split("\n")

validwords = []
for word in words:
	if (len(word) >= 4):
		validwords.append(word.lower())

answers = []
for word in validwords:
	if checkword(word,target,musthave):
		answers.append(word)

for answer in answers:
	#if answer.count(musthave):
	print answer