#!/usr/bin/bash


INPUT=$1 # Could be file or a folder
OUTPUT=$2
headPath="$kashPar/dependencies/headcomputation-1.8"
vibPath="$kashPar/dependencies/vibhakticomputation-2.3.2"

count=0
if [[ -d $INPUT ]]; then
	for file in $INPUT/*
	do
	count=$[$count + 1]
	python tokeniser.py "--input-file" "$file" "--output-file" "$OUTPUT/output.tkn$count"
	crf_test "-m" "../models/posTagging.mo" "$OUTPUT/output.tkn$count" | cut -f1,12 > "$OUTPUT/output.pos$count"
	crf_test "-m" "../models/chunking.mo" "$OUTPUT/output.pos$count" > "$OUTPUT/output.chunk$count"
	python bio2ssf.py "$OUTPUT/output.chunk$count" > "$OUTPUT/output.ssf$count"
	perl "$headPath/headcomputation.pl" "--path=$headPath" "-i" "$OUTPUT/output.ssf$count" > "$OUTPUT/output.head$count"
	perl "$vibPath/vibhakticomputation.pl" "--path=$vibPath" "-i" "$OUTPUT/output.head$count" > "$OUTPUT/output.vib$count"
	python ssf2conll.py "$OUTPUT/output.vib$count" > "$OUTPUT/output.conll$count"
	java "-jar" "maltparser-1.7.2.jar" "-c" "goldFeats.mco" "-i" "$OUTPUT/output.conll$count" "-o" "$OUTPUT/output.parse$count" "-m" "parse"		
	done
elif [[ -f $INPUT ]]; then
	python tokeniser.py "--input-file" "$INPUT" "--output-file" "$OUTPUT/output.tkn"
	crf_test "-m" "../models/posTagging.mo" "$OUTPUT/output.tkn" | cut -f1,12 > "$OUTPUT/output.pos"
	crf_test "-m" "../models/chunking.mo" "$OUTPUT/output.pos" > "$OUTPUT/output.chunk"
	python bio2ssf.py "$OUTPUT/output.chunk" > "$OUTPUT/output.ssf"
	perl "$headPath/headcomputation.pl" "--path=$headPath" "-i" "$OUTPUT/output.ssf" > "$OUTPUT/output.head"
	perl "$vibPath/vibhakticomputation.pl" "--path=$vibPath" "-i" "$OUTPUT/output.head" > "$OUTPUT/output.vib"
	python ssf2conll.py "$OUTPUT/output.vib" > "$OUTPUT/output.conll"
	java "-jar" "maltparser-1.7.2.jar" "-c" "intraChunkParser.mco" "-i" "$OUTPUT/output.conll" "-o" "$OUTPUT/output.parse" "-m" "parse"
else
	echo "Please specify the required valid argument i.e., <File> or <Directory>"
	exit 1
fi
