#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import sys
import codecs
import string
from itertools import tee, islice, chain, izip

path = sys.argv[1]
fd = codecs.open(path,"r",encoding="utf-8")
txt = fd.read()
newtxt = []
punctuation = [".", ",", u"¿", "?", u"¡", "!", "\"", "'", "_", "(", ")"]
open_punct = [u"¿", u"¡","(","\"", "_"]

lines = txt.split("\n")

for line in lines:
	## Normalizes the text in case not all punctuations are preceeded by a whitespace
	# Added in version 2
	normLine = []
	newline = ""
	prevchar = ""
	for char in line:
		#print char
		if any (c in char for c in punctuation) and prevchar != "":
			if prevchar != " ":
				normLine.append(" ")
				normLine.append(char)
				prevchar = char
				prevpunc = char
			else:
				normLine.append(char)
				prevchar = char
		elif any (c in prevchar for c in punctuation) and char != " ":
			normLine.append(" ")
			normLine.append(char)
			prevchar = char
		else:
			normLine.append(char)
			prevchar = char

	newline = ("".join(normLine))
	#print "Normalized line is :"
	#print newline
	#################
	result =[]
	words = newline.split()
	pos = 0
	prevw= ""
	initpunct = 0
	invcomas = 0
	for word in words:
		#print word
		if any(p in word for p in punctuation) :
			## Added version 2 frontal punctuation rule
			if any(i in word for i in open_punct) and initpunct == 0 and invcomas == 0:
				#print "cond 1"
				result.append(word)
				pos = len(result) -1
				prevw = word
				initpunct = 1
				if word == "\"":
					invcomas = 1
			else:
				#print "cond 2", word
				newword = prevw + word
				#print newword
				if len(result) != 0 :
					#print "2a"
					result[pos] = newword
					prevw = newword
				else:
					#print "2b"
					result.append(newword)
			#print "Punctuation is = ", newword
		elif initpunct == 1 :
			#print "cond 3"
			#print "cond 2 = ", word
			#print "prev = ", prevw
			newword = prevw + word
			if len(result) != 0:
				result[pos] = newword
				#print "cond 4"
				prevw = newword
				initpunct = 0
			else:
				result.append(newword)
				prevw = newword
				initpunct = 0
		else:
			#print "cond 4"
			result.append(word)
			pos = len(result) -1
			prevw = word
			#print "Word is =", word

	newtxt.append(" ".join(result))

f = open(sys.argv[2], "w")
f.write("\n".join(newtxt).encode("utf-8"))
#f.write(str(result))

f.close()
fd.close()