#!/bin/sh

TEMP=$(cat temp.txt)
HUMID=$(cat humid.txt)

sed "s/humidity/$HUMID/g" src.html > index2.html
sed "s/!!!!!/$TEMP/g" index2.html > index.html
rm index2.html
