#!/usr/bin/env python -*- coding: utf-8 -*-

def ssf2conll (sentence):
	"""1	koshur	_	JJP	JJ	_	2	nmod	_	_"""
	idx = int()
	for node in sentence:
		if node.split("\t")[0].isdigit():
			idx += 1
			features = re.search("<fs (.*?)>", node).group(1)
			tag = word = chunkType = str()
			for feature in features.split():
				if feature.strip().startswith("af="):
					tag = feature.split(",")[1]
				elif feature.strip().startswith("head="):
					word = feature.strip().split("=")[-1]
				elif feature.strip().startswith("name="):
					chunkType = re.sub('[0-9]','',feature.strip().split("=")[-1])
				else:pass
			assert tag != word != chunkType != ''
			yield "\t".join((str(idx),word,"_",chunkType,tag,"_","_","_","_","_"))
			

if __name__ == "__main__":
	
	import re
	import sys
	
	try:
		assert sys.argv[1]
	except:
		"Please specify the required arguments"
	else:
		inputFile = open(sys.argv[1]).read()
		ssfSentences = re.findall("<Sentence id=.*?>(.*?)</Sentence>",inputFile, re.S)
		
		for sentence in ssfSentences:
			ssf2conll(sentence.strip().split("\n"))
			print "\n".join(ssf2conll(sentence.strip().split("\n")))
			print
