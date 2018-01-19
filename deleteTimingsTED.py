import re
import sys
import codecs
from itertools import tee, islice, chain, izip

path = sys.argv[1]
fd = codecs.open(path,"r",encoding="utf-8")
txt = fd.read()
result = []

sentences = txt.split("\n\n")

for sentence in sentences:
	chunks = sentence.split("|")
	#print chunks
	for chunk in chunks:
		#print chunk
		if re.match(r"\D\D\D\D", chunk):
			#print chunk
			if chunk != "\n":
				result.append(chunk)
			else:
				print "Return has been found"

f = open(sys.argv[2], "w")
f.write(" ".join(result))

f.close()
fd.close()