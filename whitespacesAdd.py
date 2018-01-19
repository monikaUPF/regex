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
	normLine = []
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

	newtxt.append("".join(normLine))

f = open(sys.argv[2], "w")
f.write("".join(newtxt).encode("utf-8"))


f.close()
fd.close()