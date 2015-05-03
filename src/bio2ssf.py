#!/usr/bin/env python -*- coding: utf-8 -*-

__Author__ = "Riyaz Ahmad Bhat"
__Version__ = "1.0"

import re
import sys

def convertToSsf(bioSentence):
	typeCount = list()
	nonTerminalId = terminalId = int()
	for idx, line in enumerate(bioSentence):
		word,tag,bio = line.split("\t")
		boundary,chunkType = bio.split("-")
		if boundary == "B":
			nonTerminalId += 1
			if idx:
				yield "\t))"
			typeCount.append(chunkType)
			count = typeCount.count(chunkType)
			terminalId = 1
			nodeCount = str(nonTerminalId)+"."+str(terminalId)
			
			if count is 1:
				yield "\t".join((str(nonTerminalId),"((",chunkType,"<fs name='"+chunkType+"'>"))
			else:
				yield "\t".join((str(nonTerminalId),"((",chunkType,"<fs name='"+chunkType+str(count)+"'>"))
			yield "\t".join((str(nodeCount),word,tag,"<fs af='"+word+","+tag+",,,,,,' name='"+word+"'>"))
		else:
			terminalId += 1
			nodeCount = str(nonTerminalId)+"."+str(terminalId)
			yield "\t".join((str(nodeCount),word,tag,"<fs af='"+word+","+tag+",,,,,,' name='"+word+"'>"))
	yield "\t))"

if __name__ == "__main__":

	try:
		assert sys.argv[1]
	except Exception, error:
		print error,"Please specify the required argument"
	else:
		
		sentences = re.split("\n\n", open(sys.argv[1]).read().strip())
		for sentId, sentence in enumerate(sentences):
			sentenceTag = '<Sentence id="'+str(sentId+1)+'">'
			print "\n".join((sentenceTag,"\n".join(convertToSsf(sentence.strip().split("\n"))),"</Sentence>\n"))
