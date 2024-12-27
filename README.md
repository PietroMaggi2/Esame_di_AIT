# Esame\_di\_AIT
Buongiorno! Questo repository GitHub contiene gli script degli esercizi svolti per l'esame di Abilità Informatiche e Telematiche di Pietro Maggi.

Gli esercizi che ho scelto di svolgere sono i seguenti:

\- Il terzo esercizio di Bash, il cui script è contenuto nella directory "esercizio3\_bash";

\- Il quarto esercizio di Bash, il cui script è contenuto nella directory "esercizio4\_bash";

\- Il quinto esercizio di Bash, il cui script è contenuto nella directory "esercizio5\_bash";

\- Il sesto esercizio di Bash, il cui script è contenuto nella directory "esercizio6\_bash";

\- L'esercizio di Python proposto, il cui script è contenuto nella directory "esercizio\_python\_esame".

NOTA: Gli esercizi di Bash vanno eseguito con il comando ./nomefile.sh, mentre l'esercizio di Python va eseguito con il comando python nomefile.py

## Esercizio 3 di Bash
Il terzo esercizio di Bash proposto richiede di contare il numero di files, non directories, presenti nella directory corrente. Per far questo suggerisce di creare una funzione file\_count che, attraverso l'utilizzo dei comandi ls, grep e wc, esegue la richiesta.

Lo script è stato realizzato nel file "es3.sh".

Visto che lo script viene eseguito in una cartella di prova ho deciso di far generare un numero casuale compreso fra 1 e 10 di files e directories allo script (questi sono identificati dal nome filei, dirj, con i e j che vanno da 0 al numero random generato - 1). Per rendere poi completamente indipendenti le varie esecuzioni ho anche inserito l'eliminazione dei files/directories di prova all'inizio di ogni esecuzione.

Il numero di file presenti (che in questo caso corrisponderà al numero casuale generato + 1, lo script) verrà stampato a schermo con la dicitura "il numero di file presenti in questa directory è:"

NOTA: Alla prima esecuzione, vista l'assenza di files/directories di prova apparirà il seguente warning:

rm: cannot remove 'file\*': No such file or directory   

rmdir: failed to remove 'dir\*': No such file or directory

## Esercizio 4 di Bash
Il quarto esercizio di Bash proposto è una continuazione del terzo esercizio. In particolare, viene richiesto di modificare la funzione file\_count, permettendo di passare come argomento una directory diversa da quella corrente dove andare a fare il conteggio dei file.

Lo script è stato realizzato nel file "es4.sh".

Per prima cosa la funzione controlla che il parametro passato sia effettivamente una directory. Nel caso in cui non lo sia visualizza a schermo la seguente scritta "L' elemento passato come argomento non è una directory!".

Nel caso in cui il parametro sia effettivamente una directory viene visualizzato a schermo il nome di questa con i :, e a capo il numero di files presenti in essa. Come richiesto dall'esercizio la funzione file\_count viene chiamata con la directory "/etc", "/var" e "/usr/bin".

## Esercizio 5 di Bash
Il quinto esercizio di Bash proposto necessita della creazione di un file contenente i primi 10 numeri interi. Questo file è stato chiamato file1 e all'inizio dello script viene svuotato, se già presente, per rendere indipendenti le varie esecuzioni. 

Lo script è stato realizzato nel file "es5.sh".

Lo script valuta la somma dei numeri interi contenuti nel file con il comando awk e con l'implementazione della formula di Gauss. I risultati vengono riportati a schermo nel seguente modo:

Somma ottenuta con il comando awk:

"risultato ottenuto con il comando awk"

Somma ottenuta con la formula di Gauss:

"risultato ottenuto con la formula di Gauss"

NOTA: Lo script è stato realizzato in modo tale da permettere l'esecuzione anche con numeri diversi da 10 come limite superiore. Per modificare questo limite basta entrare nel file script e inserire un valore diverso da associare alla variabile n.

## Esercizio 6 di Bash
Il sesto esercizio di Bash proposto parte con la realizzazione di un file contenente questo testo:

\# control of memory    requirements

BoundaryLayerFactor     3.0

MaxMem                  512

MaxMemPerParticle       240

PredPeakFactor          0.8

Il file contenente questo testo è stato chiamato file1 e viene svuotato all'inizio dello script per rendere indipendenti le varie esecuzioni del programma.

Lo script è stato realizzato nel file "es6.sh".

Questo file viene poi modificato e risalvato come richiesto utilizzando il comando awk (in particolare 512, il valore di MaxMem, viene sostituito con 1024). 

## Esercizio di Python
L'esercizio di Python proposto si articola in molti punti che verranno trattati singolarmente qui di seguito.

Lo script completo dell'esercizio è stato realizzato nel file "espython.py".

Il file "file2\_Groups\_AGN-wWU\_500Mpc\_Data.txt" che viene passato con lo script contiene i dati delle strutture ottenuti nella simulazione idrodinamica cosmologica.

### Primo punto
Il primo punto chiede di realizzare il grafico della massa di materia oscura degli aloni ottenuti in funzione della loro massa barionica e di cercare di ottenere anche un fit lineare significativo dei dati.

NOTA: Vista la presenza di una struttura con massa barionica e massa di materia oscura due ordini di grandezza più alte rispetto agli altri aloni ottenuti nella simulazione, ho deciso di riportare il grafico in scala log-log. Esso viene salvato nel file "FiguraDM\_MassaBarionica\_fitlineare.png".

Il fit lineare ottenuto non sembra interpolare bene i dati in tutto il range di massa barionica. Questo suggerisce che la correlazione fra le due grandezze non sia costante, ma vari a seconda dei regimi di massa considerati.

### Secondo punto
Il secondo punto dell'esercizio chiede di concentrarsi sulla struttura più massiva e di valutare le distanze di tutti gli altri aloni da questa. Dopo aver fatto ciò si grafica l'andamento della massa della struttura in funzione di questa distanza. 

NOTA: Anche in questo caso, come prima, per poter apprezzare a pieno la distribuzione delle strutture è necessario mettere l'asse delle masse in scala logaritmica. L'asse delle distanze risulta sensato sia in scala logaritmica che in scala lineare. Per questo motivo ho scelto di realizzare due grafici, uno in scala log-lin, salvato nel file "FiguraDistanza\_Massatotale\_log\_lin.png" e uno in scala log-log, salvato nel file "FiguraDistanza\_Massatotale\_log\_log.png".

### Terzo punto
Il terzo punto dell'esercizio chiede di realizzare un istogramma, salvato nel file "istogramma.png".

L'istogramma riporta la distribuzione di massa di materia oscura degli aloni, calcolando anche la media e la mediana di questi valori. Media e mediana vengono riportate sul grafico come rette verticali e i loro valori sono indicati nella legenda realizzata in alto a destra.

### Quarto punto
Il quarto punto chiede di realizzare tre plot in un'unica figura, salvata nel file "proiezioni.png".

Questi tre plot riportano la distribuzione proiettata degli aloni sui tre piani bidimensionali, XY, ZY, XZ. Per differenziare le caratteristiche delle strutture sui grafici ho fatto variare il colore dei punti in funzione della massa di gas delle strutture, e la grandezza di questi in funzione della massa stellare.

### Quinto punto
Il quinto punto richiede di graficare la massa del buco nero centrale della struttura in funzione della massa stellare, quando la prima è maggiore di 8 x 10^5 Msun/h. Questo grafico viene riportato nel file "FiguraBH\_Massastellare.png". 

NOTA: Come prima, vista la distribuzione delle masse in diversi ordini di grandezza gli assi vengono riportati in scala logaritmica.

Inoltre, l'esercizio chiede di realizzare un fit lineare dei dati. Il fit risulta sensato, indicando la presenza di una correlazione lineare fra massa del buco nero centrale e massa stellare totale in questo range. Questo potrebbe indicare che la formazione stellare nell'intera struttura è perturbata dal buco nero supermassivo centrale.

### Sesto punto
L'ultimo punto dell'esercizio di Python chiede di realizzare degli istogrammi bidimensionali, riportando sull'asse delle x la distribuzione di massa totale delle strutture, e sull'asse delle y la distanza di queste dagli aloni con massa di gas superiore a 3.07 x 10^9 Msun/h. in totale sono quindi generati 5 istogrammi, uno per ogni alone (salvati nei file 'ist\_bid\_alone\_i.png', con i che va da 1 a 5) più uno ottenuto dalla somma dei precedenti, salvato nel file 'ist\_bid\_totale.png'.

NOTA: Come colormap ho scelto la gradazione di blu.




