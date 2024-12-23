#!/bin/bash

function file_count (){		#Questa funzione conta il numero di file presenti nella directory corrente
	echo "Il numero di file presenti in questa directory è:"	
	ls -l|grep "^-"|wc -l  	#ls -l lista tutti i file/directory presenti. I file sono individuati con il - iniziale, quindi cerco
				#le righe contenenti quel carattere come primo carattere. Successivamente conto queste righe filtrate
				#e le stampo a schermo con wc -l
}

a=$((1 + RANDOM % 10))		#Si generano due numeri interi casuali fra 1 e 10 per generare i file e le directory per il test
b=$((1 + RANDOM % 10))

for (( i = 1; i < $a; i++ ))	#Creazione dei file
do
	touch file$i
done

for (( j = 1; j < $b; j++ ))	#Creazione delle directory
do
	mkdir dir$j
done

file_count

exit 0
