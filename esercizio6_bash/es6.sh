#!/bin/bash

touch file1	#Creazione del file se non esiste già
> file1		#Si svuota il file nel caso esista già

echo -e "# control_of_memory	requirements\nBoundaryLayerFactor	3.0\nMaxMem			512\nMaxMemPerparticle	240\nPredPeakFactor		0.8">file1	#Redireziona nel file1

awk -i inplace '{if ($1=="MaxMem") {$2= "			1024"} ; print $0}' "file1"	
# -i inplace mi permette di fare la modifica in loco. La modifica consiste nel cambiare il valore della seconda colonna di MaxMem

exit 0
