#!/bin/sh

XLSX=$(ls ./spreadsheets/ | grep xlsx | tail -1)
echo $XLSX
PNG=$(ls ./spreadsheets/ | grep png | tail -1)
echo $PNG
sed "/Bảng tính/a <a href="./spreadsheets/$XLSX" download> <p> $XLSX </p> </a>" data.html > data2.html
sed "/Biểu đồ/a <img src="./spreadsheets/$PNG"> " data2.html > data.html
rm data2.html
