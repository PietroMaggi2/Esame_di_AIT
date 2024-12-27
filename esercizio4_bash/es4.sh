#!/bin/bash

function file_count {		#Questa funzione restituisce il numero di file contenuti in una directory passata come parametro
	local dire=$1		#Il parametro passato viene inserito nella variabile locale dire
	if [ -d $dire ]		#Controllo sul fatto che il parametro sia effettivamente il path di una directory
	then
		echo $dire:				
        	ls -l $dire|grep "^-"|wc -l>file1	#ls -l lista tutti i file/directory presenti. grep "-" isola i file. wc -l li
		local a=`cat file1`			#conta.
		echo $a files				#Si passa il numero di file a un file1 e poi a una variabile locale per poter
		rm file1				#stampare a schermo 'numerofile' files. Infine si rimuove il file creato.
	else
		echo L\'elemento passato come argomento non è una directory!
		exit 1					#Messaggio di errore con exit status diverso da 0 se l'argomento passato non
	fi						#è una directory.
}


file_count /etc
file_count /var
file_count /usr/bin

exit 0

#Se la valutazione da parte della funzione va a buon fine lo script termina con un exit status di 0.
#Se l'elemento passato come parametro non risulta essere il path di una directory si termina l'esecuzione con un exit status di 1.

