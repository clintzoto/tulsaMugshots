#!/bin/bash
find . -name '*.jpg' -type f -print | while read file; do 
    hash=$(md5sum $file | awk '{print $1}') 
    echo $hash 
    cp $file thumbs/${file%.*}-$hash.${file/*.} 
done

