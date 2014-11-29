#!/usr/bin/env python -*- coding: utf-8 -*-

__Author__ = "Riyaz Ahmad Bhat"
__Version__ = "1.0"

#ApaNe	More	Apa	Ap	A	e	Apa	Ap	A		PRP
#ridZhana	More	ridZ	rid	ri	a	ridZ	rid	ri	r	NN

def prefix(token):

	if len(token)>=4:
		yield token[-4:]
	else:
		yield "LL"

	if len(token)>=3:
		yield token[-3:]
	else:
		yield "LL"

	if len(token)>=2:
		yield token[-2:]
	else:
		yield "LL"
	try:
		yield token[-1]
	except:
		yield "_"

def suffix(token):

	if len(token)>=4:
		yield token[:4]
	else:
		yield "LL"
	
	if len(token)>=3:
		yield token[:3]
	else:
		yield "LL"

	if len(token)>=2:
		yield token[:2]
	else:
		yield "LL"

	try:
		yield token[0]
	except:
		yield "_"

def length(word):
	if len(word) >= 4:
		yield "More"
	else:
		yield "Less"

def affixes (word):
	word = word.decode("utf-8",)
	features = "\t".join((word, "\t".join(length(word)), "\t".join(prefix(word)), "\t".join(suffix(word))))
	return features.encode("utf-8")
