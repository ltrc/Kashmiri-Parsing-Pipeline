Kashmiri-Parsing-Pipeline
=========================

A toolkit for Kashmiri which includes a portion of Kashmiri Dependency treebank and a dependency parsing pipeline with a POS-tagger, a Chunker and an Intra-chunk Dependency Parser.

__How to use?__
```
bash dependencyParser.sh <input (file|directory)> <output (directory)>
```
__Dependencies__

Install the following:
```
Maltparser and CRF++
```

Set the environment variable kashPar to Kashmiri Parsing directory in ~/.bashrc as:
```
export kashPar="/home/usr/Kashmiri-Parsing-Pipeline"
```
