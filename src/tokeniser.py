#!/usr/bin/env python -*- coding: utf-8 -*-

import re
import os
import sys
import string
import argparse
import letterBasedAffixes as tkn

def tokenise (inFile, outFile):
	for segment in inFile:
		if segment == "\n":
			continue
		else:
			lines = re.sub("۔|؟|!",' ۔\n', segment.strip()).strip()
			for line in lines.split("\n"):
				line = line.strip().decode("utf-8")
				words = re.split("[ ]+", line.strip())
				for word in words:
					if word != '':
						outFile.write("\t".join((word.encode("utf-8"), tkn.affixes(word)))+'\n')
				outFile.write('\n')

def parse_options():

  parser = argparse.ArgumentParser(description="%%% Kashmiri Tokeniser. %%%")
  parser.add_argument('--input-file', dest='input', required=True, help='raw text file')
  parser.add_argument('--output-file', dest='output', required=True, help='output tokenised file in tnt format')

  args = parser.parse_args()

  return args

def main():

	options = parse_options()

	try:
		assert os.path.isfile (options.input)
	except Exception, e:
		print "\n\t\t\t'"+options.input+"' is not a file.\n"
		return

	inputFile = open(options.input)
	tokenise(inputFile, open(options.output,'w'))
	

if __name__ == "__main__":
	main()
