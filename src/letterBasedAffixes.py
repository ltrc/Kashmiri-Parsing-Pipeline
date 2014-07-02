#!/usr/bin/env python -*- coding: utf-8 -*-

__Author__ = "Riyaz Ahmad Bhat"
__Version__ = "1.0"

def prefix(token):
	global features
	if len(token)>=4:
		features += "\t"+"".join(token[-4:])
	else:
		features += "\tLL"

	if len(token)>=3:
		features += "\t"+"".join(token[-3:])
	else:
		features += "\tLL"

	if len(token)>=2:
		features += "\t"+"".join(token[-2:])
	else:
		features += "\tLL"

	features += "\t"+token[-1]

def suffix(token):
	global features
	if len(token)>=4:
		features += "\t"+"".join(token[:5])
	else:
		features += "\tLL"

	if len(token)>=3:
		features += "\t"+"".join(token[:4])
	else:
		features += "\tLL"

	if len(token)>=2:
		features += "\t"+"".join(token[:3])
	else:
		features += "\tLL"

	features += "\t"+token[0]

def affixes (word):
	global features
	features = word
	if len(word) >= 4:
		features += "\tMore"
	else:
		features += "\tLess"	
	prefix(word)
	suffix(word)

	return features.encode("utf-8")
