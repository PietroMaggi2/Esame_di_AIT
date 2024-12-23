#!/bin/bash

if [ -e "./shadow" ]	#Qui controllo che il file shadow esista in questa directory
then
	echo -e "Shadow passwords are enabled\n"
	cat "./shadow"

	if [ -w "./shadow" ]	#Se shadow esiste controllo che sia modificabile
	then
		echo -e "\nYou have permission to edit ./shadow"
	else
		echo -e "\nYou do NOT have permission to edit ./shadow"
		exit 2
	fi
else
	exit 1
fi

exit 0

#Ritorno 0 se lo script è andato a buon fine
#Ritorno 1 se il file non esiste
#Ritorno 2 se il file esiste ma non è modificabile
