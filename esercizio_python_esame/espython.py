import numpy as np
import matplotlib.pyplot as plt
import math as m


def plot(x,y,nomex,nomey,udmx,udmy,scalax,scalay,marker,colore,nomefigura):
    '''
    Questa funzione permette di produrre un grafico in base alle informazioni date come parametri
    ---------------------------------------------------------------------------------------------
    Parametri:
    x: Array di dati da graficare sull'asse delle x
    y: Array di dati da graficare sull'asse delle y
    nomex: Nome dell'asse delle x
    nomey: Nome dell'asse delle y
    udmx: Unità di misura delle x
    udmy: Unità di misura delle y
    scalax: Scala dell'asse delle x (lineare, log...)
    scalay: Scala dell'asse delle y (lineare, log...)
    marker: Marker dei punti sul plot
    colore: Colore dei punti sul plot
    nomefigura: Nome del file dove salvare il grafico
    '''
    fig, ax = plt.subplots()
    fig.set_size_inches(18,10)
    ax.set_title('Grafico di {} in funzione di {} in scala {}-{}'.format(nomey,nomex,scalay,scalax), fontsize=20)
    ax.set_xlabel('{} [{}]'.format(nomex, udmx), fontsize=15)
    ax.set_ylabel('{} [{}]'.format(nomey,udmy), fontsize=15)
    ax.set_xscale('{}'.format(scalax))
    ax.set_yscale('{}'.format(scalay))
    ax.scatter(x, y, marker='{}'.format(marker), color='{}'.format(colore))
    ax.tick_params(axis='both', right=True, top=True, direction='in')
    fig.savefig("{}".format(nomefigura))

def plot_con_fit(x,y,yfit,nomex,nomey,udmx,udmy,scalax,scalay,marker,colore,colorefit,nomefigura):
    '''
    Questa funzione permette di produrre un grafico in base alle informazioni date come parametri
    ---------------------------------------------------------------------------------------------
    Parametri:
    x: Array di dati da graficare sull'asse delle x
    y: Array di dati da graficare sull'asse delle y
    yfit: Array di dati del fit lineare
    nomex: Nome dell'asse delle x
    nomey: Nome dell'asse delle y
    udmx: Unità di misura delle x
    udmy: Unità di misura delle y
    scalax: Scala dell'asse delle x (lineare, log...)
    scalay: Scala dell'asse delle y (lineare, log...)
    marker: Marker dei punti sul plot
    colore: Colore dei punti sul plot
    colorefit: Colore del fit lineare
    nomefigura: Nome del file dove salvare il grafico
    '''
    fig, ax = plt.subplots()
    fig.set_size_inches(18,10)
    ax.set_title('Grafico di {} in funzione di {} in scala {}-{}'.format(nomey,nomex,scalay,scalax), fontsize=20)
    ax.set_xlabel('{} [{}]'.format(nomex, udmx), fontsize=15)
    ax.set_ylabel('{} [{}]'.format(nomey,udmy), fontsize=15)
    ax.set_xscale('{}'.format(scalax))
    ax.set_yscale('{}'.format(scalay))
    ax.scatter(x, y, marker='{}'.format(marker), color='{}'.format(colore))
    ax.plot(x,yfit,color='{}'.format(colorefit))
    ax.tick_params(axis='both', right=True, top=True, direction='in')
    fig.savefig("{}".format(nomefigura))

def histo(x,nomehist,nomefigura):
    '''
    Questa funzione restituisce l'istogramma dell'array in input, con indicate anche la media e la mediana, nel file indicato
    -------------------------------------------------------------------------------------------------------------------------
    Parametri:
    x: Array di dati che si vogliono istogrammare
    nomehist: Titolo dell'istogramma e dell'asse x
    nomefigura: Nome del file dove viene salvato il grafico
    '''
    hist, bins = np.histogram(x)
    media = np.mean(x)
    mediana = np.median(x)
    fig, ax = plt.subplots()
    fig.set_size_inches(18,10)
    ax.set_title('Istogramma di {}'.format(nomehist), fontsize=20)
    ax.set_xlabel('{}'.format(nomehist), fontsize=15)
    ax.set_ylabel('Numero di strutture', fontsize=15)
    ax.stairs(hist,bins)
    ax.axvline(media,color='r',label='Media = {:.3f}'.format(round(media,3)))
    ax.axvline(mediana,color='g', label='Mediana = {}'.format(round(mediana,3)))
    ax.set_xticks(bins)
    ax.tick_params(axis='both', right=True, top=True, direction='in')
    ax.legend()
    fig.savefig("{}".format(nomefigura))

#SCRIPT PRINCIPALE

data_filename = '/home/pietromg/esame/Esame_di_AIT/esercizio_python_esame/file2_Groups_AGN-wWU_500Mpc_Data.txt'
data = np.loadtxt(data_filename, unpack = True)
total_mass = data[0]    #Massa totale. Misurata in 10^10 Msun/h
gas_mass = data[1]      #Massa di gas. Misurata in 10^10 Msun/h
dm_mass = data[2]       #Massa di materia oscura. Misurata in 10^10 Msun/h
stellar_mass = data[3]  #Massa di stelle. Misurata in 10^10 Msun/h
posx = data[5]          #Posizione x. Misurata in ckpc/h
posy = data[6]          #Posizione y. Misurata in ckpc/h
posz = data[7]          #Posizione z. Misurata in ckpc/h

#PRIMO PUNTO: Grafico della massa di materia oscura in funzione di quella barionica in scala lineare e logaritmica (con fit lineare)

baryonic_mass = gas_mass + stellar_mass
m,q = np.polyfit(baryonic_mass,dm_mass,1)
y = m*baryonic_mass + q

plot_con_fit(baryonic_mass,dm_mass,y,'Massa barionica','Massa di materia oscura','10^10 Msun/h','10^10 Msun/h','linear','linear','x','r','b','FiguraDM_MassaBarionica_lineare.png')

plot(baryonic_mass,dm_mass,'Massa barionica','Massa di materia oscura','10^10 Msun/h','10^10 Msun/h','log','log','.','b','FiguraDM_MassaBarionica_log.png')

#SECONDO PUNTO: Grafico della distanza delle strutture dalla più massiva
#Per visualizzare bene la distribuzione mettere l'asse y in scala logaritmica. L'asse x può essere lasciato in scala lineare.

mask = np.where(total_mass == max(total_mass))[0]
posxmax = float(posx[mask][0])
posymax = float(posy[mask][0])
poszmax = float(posz[mask][0])

distance = np.sqrt(np.square(posx - posxmax) + np.square(posy - posymax) + np.square(posz - poszmax))
plot(distance,total_mass,'Distanza dalla struttura più massiva','Massa totale','ckpc/h','10^10 Msun/h','linear','log','x','r','FiguraDistanza_Massatotale_log_lin.png')
plot(distance,total_mass,'Distanza dalla struttura più massiva','Massa totale','ckpc/h','10^10 Msun/h','log','log','x','r','FiguraDistanza_Massatotale_log_log.png')


#TERZO PUNTO: Istogramma della distribuzione di materia oscura

histo(np.log10(dm_mass),'logaritmo in base dieci della massa di materia oscura', 'istogramma.png')




