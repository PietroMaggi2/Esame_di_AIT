#!/bin/bash

touch file1					#Creazione del file se non è già presente
> file1						#Il file viene svuotato nel caso in cui esistesse già

n=10						#Numero massimo da considerare nella somma di interi
for ((i=0 ; i<=$n ; i++))
do
	echo $i>>file1				#Si riempie il file con tutti i numeri interi da 0 a n
done

echo Somma ottenuta con il comando awk:

awk '{ sum += $1 } END { print sum }' file1	#Somma fatta con il comando awk
let m=n+1
let sum=n*m/2					#Somma fatta con la formula di Gauss
echo Somma ottenuta con la formula di Gauss:
echo $sum

exit 0
