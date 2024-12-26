#!/bin/bash

function file_count {		#Questa funzione restituisce il numero di file contenuti in una directory passata come parametro
	dire=$1
	if [ -d $dire ]		#Controllo sul fatto che il parametro sia effettivamente il path di una directory
	then
		echo $dire:	
        	ls -l $dire|grep "^-"|wc -l
	else
		echo L\'elemento passato come argomento non è una directory!
		exit 1
	fi
}


file_count /etc
file_count /var
file_count /usr/bin

exit 0

#Se la valutazione da parte della funzione va a buon fine lo script termina con un exit status di 0.
#Se l'elemento passato come parametro non risulta essere il path di una directory si termina l'esecuzione con un exit status di 1.

