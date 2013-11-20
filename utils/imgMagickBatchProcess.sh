#!/bin/bash
#for f in *.jpg; do convert $f -resize 85x85 $f ./subfFolderName/$f; done
for f in *.jpg; do convert $f -resize 85x85 $f; done #overrites everything in the directory
#for f in *.jpg; do convert $f -shave 112x34 ./thumbs85x85/$f; done
