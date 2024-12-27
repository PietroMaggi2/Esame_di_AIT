import numpy as np
import matplotlib.pyplot as plt
import math as m
import matplotlib as mpl


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

def plot_con_fit(x,y,xfit,yfit,mfit,qfit,nomex,nomey,udmx,udmy,scalax,scalay,marker,colore,colorefit,nomefigura):
    '''
    Questa funzione permette di produrre un grafico in base alle informazioni date come parametri
    ---------------------------------------------------------------------------------------------
    Parametri:
    x: Array di dati da graficare sull'asse delle x
    y: Array di dati da graficare sull'asse delle y
    xfit: Array dei dati dell'asse x del fit lineare
    yfit: Array di dati dell'asse y fit lineare
    mfit: Il coefficiente angolare del fit lineare
    qfit: L'intercetta del fit lineare
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
    ax.plot(xfit,yfit,color='{}'.format(colorefit),label='m= {}, q= {}'.format(round(mfit,3),round(qfit,3)))
    ax.tick_params(axis='both', right=True, top=True, direction='in')
    ax.legend(loc='upper left')
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

def subplot(x,y,z,grandezze,colori):
    '''
    Questa funzione restituisce le proiezioni degli aloni sui tre piani cartesiani
    ------------------------------------------------------------------------------
    Parametri:
    x: Array delle posizioni in x
    y: Array delle posizioni in y
    z: Array delle posizioni in z
    grandezze: Array di variazione della grandezza dei punti (scala con la massa stellare)
    colori: Arrat di variazione del colore dei punti (scala con la massa di gas)
    '''
    fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2,layout='constrained')
    fig.set_size_inches(18,10)
    ax1.set_title('Proiezione degli aloni sul piano XY', fontsize=20)
    ax2.set_title('Proiezione degli aloni sul piano ZY', fontsize=20)
    ax3.set_title('Proiezione degli aloni sul piano XZ', fontsize=20)
    ax1.set_ylabel('Posizione sull\'asse delle y [ckpc/h]', fontsize=15)
    ax2.set_xlabel('Posizione sull\'asse delle z [ckpc/h]', fontsize=15)
    ax3.set_xlabel('Posizione sull\'asse delle x [ckpc/h]', fontsize=15)
    ax3.set_ylabel('Posizione sull\'asse delle z [ckpc/h]', fontsize=15)
    pos1 = ax1.scatter(x, y,s=grandezze,color=colori)
    ax2.scatter(z,y,s=grandezze,color=colori)
    pos3 = ax3.scatter(x,z,s=grandezze,color=colori)
    ax1.tick_params(axis='both', right=True, top=True, direction='in')
    ax2.tick_params(axis='both', right=True, top=True, direction='in')
    ax3.tick_params(axis='both', right=True, top=True, direction='in')
    fig.delaxes(ax4)
    fig.colorbar(pos1)
    fig.colorbar(pos3)
    fig.text(0.55,0.3,'NOTA: La grandezza dei punti scala con la massa stellare. Il colore scala con la massa di gas', fontsize = 12)
    fig.savefig("proiezioni.png")

def istbid(x,y,binsx,binsy,titolo,nome):
    '''
    Questa funzione restituisce l'istogramma bidimensionale degli array x e y
    -------------------------------------------------------------------------
    Parametri:
    x: Array da istogrammare sull'asse x
    y: Array da istogrammare sull'asse y
    binsx: Estremi dei bins sull'asse x
    binsy: Estremi dei bins sull'asse y
    titolo: Titolo del grafico
    nome: Nome del file dove salvare il grafico
    '''
    fig,ax = plt.subplots()
    ax.set_title('Istogramma bidimensionale {}'.format(titolo), fontsize=20)
    ax.set_xlabel('Massa totale [10^10 Msun/h] in log10', fontsize=15)
    ax.set_ylabel('Distanze in [ckpc/h]', fontsize=15)
    fig.set_size_inches(18,10)
    h = ax.hist2d(x,y,bins=[binsx,binsy],cmap='Blues')
    #h[0] sono i valori dell'istogramma delle masse. h[1] sono gli edges delle masse. h[2] sono gli edges delle distanze.
    ax.set_xticks(h[1])
    ax.set_yticks(h[2])
    ax.tick_params(axis='x',labelrotation=90)
    fig.savefig(nome)

#SCRIPT PRINCIPALE

data_filename = '/home/pietromg/esame/Esame_di_AIT/esercizio_python_esame/file2_Groups_AGN-wWU_500Mpc_Data.txt'
data = np.loadtxt(data_filename, unpack = True)
total_mass = data[0]    #Massa totale. Misurata in 10^10 Msun/h
gas_mass = data[1]      #Massa di gas. Misurata in 10^10 Msun/h
dm_mass = data[2]       #Massa di materia oscura. Misurata in 10^10 Msun/h
stellar_mass = data[3]  #Massa di stelle. Misurata in 10^10 Msun/h
bh_mass = data[4]       #Massa del buco nero. Misurata in 10^10 Msun/h
posx = data[5]          #Posizione x. Misurata in ckpc/h
posy = data[6]          #Posizione y. Misurata in ckpc/h
posz = data[7]          #Posizione z. Misurata in ckpc/h

#PRIMO PUNTO: Grafico della massa di materia oscura in funzione di quella barionica in scala lineare e logaritmica (con fit lineare)

baryonic_mass = gas_mass + stellar_mass         #Calcolo della massa barionica
mask = np.where(baryonic_mass != 0.0)[0]        #Elimino i punti problematici
barmass_fit = baryonic_mass[mask]
dmmass_fit = dm_mass[mask]
mask = np.where(dmmass_fit != 0.0)[0]
barmass_fit = barmass_fit[mask]
dmmass_fit = dmmass_fit[mask]
barmass_fit = np.log10(barmass_fit)
dmmass_fit = np.log10(dmmass_fit)
mdm,qdm = np.polyfit(barmass_fit,dmmass_fit,1)  #Fit lineare dei dati
ydm= mdm*barmass_fit + qdm
barmass_fit = 10**(barmass_fit)
dmmass_fit = 10**(dmmass_fit)
ydm = 10**(ydm)

plot_con_fit(barmass_fit,dmmass_fit,barmass_fit,ydm,mdm,qdm,'Massa barionica','Massa di materia oscura','10^10 Msun/h','10^10 Msun/h','log','log','x','r','b','FiguraDM_MassaBarionica_fitlineare.png')

#SECONDO PUNTO: Grafico della distanza delle strutture dalla più massiva

mask = np.where(total_mass == max(total_mass))[0]   #Individuazione della struttura più massiva
posxmax = float(posx[mask][0])                      #Individuazione della posizione della struttura più massiva
posymax = float(posy[mask][0])
poszmax = float(posz[mask][0])

distance = np.sqrt(np.square(posx - posxmax) + np.square(posy - posymax) + np.square(posz - poszmax)) #Distanza da massamax
plot(distance,total_mass,'Distanza dalla struttura più massiva','Massa totale','ckpc/h','10^10 Msun/h','linear','log','x','r','FiguraDistanza_Massatotale_log_lin.png')
plot(distance,total_mass,'Distanza dalla struttura più massiva','Massa totale','ckpc/h','10^10 Msun/h','log','log','x','r','FiguraDistanza_Massatotale_log_log.png')

#TERZO PUNTO: Istogramma della distribuzione di materia oscura

histo(np.log10(dm_mass),'materia oscura [10^10 Msun/h] in log10', 'istogramma.png')

#QUARTO PUNTO: Distribuzione proiettata degli aloni

gas_mass1 = np.where(gas_mass == 0.0, 10**(-5), gas_mass)               #Individuazione dei punti problematici
stellar_mass1 = np.where(stellar_mass == 0.0, 10**(-5), stellar_mass)
gasutile = np.log10(gas_mass1) + 5.0
stellarutile = np.log10(stellar_mass1) + 5.0
cmap = plt.get_cmap('viridis')
norm = plt.Normalize(gasutile.min(), gasutile.max())
line_colors = cmap(norm(gasutile))                      #Creazione della scala colori in funzione della massa di gas
sizes = np.square(stellarutile)                         #Creazione della scala di grandezze in funzione della massa stellare
subplot(posx,posy,posz,sizes,line_colors)

#QUINTO PUNTO: Grafico della massa del buco nero corrispondente alla struttura, in funzione della massa stellare

mask = np.where(bh_mass > 8.0*10**(-5))[0]  #Individuazione dei punti per il fit
bhmass_fit = bh_mass[mask]
stellarmass_fit = stellar_mass[mask]

mask = np.where(stellarmass_fit != 0.0)[0]  #Eliminazione dei punti problematici per il fit
stellarmass_fit = stellarmass_fit[mask]
bhmass_fit = bhmass_fit[mask]
stellarmass_fit = np.log10(stellarmass_fit)
bhmass_fit = np.log10(bhmass_fit)

mbh,qbh = np.polyfit(stellarmass_fit,bhmass_fit,1)  #Fit lineare
ybh = mbh*stellarmass_fit + qbh
bhmass_fit = 10**(bhmass_fit)
stellarmass_fit = 10**(stellarmass_fit)
ybh = 10**(ybh)

plot_con_fit(stellarmass_fit,bhmass_fit,stellarmass_fit,ybh,mbh,qbh,'Massa stellare','Massa del buco nero (Massa BH > 8 x 10^5 Msun/h)','10^10 Msun/h','10^10 Msun/h','log','log','.','b','r','FiguraBH_Massastellare.png')

#SESTO PUNTO: Istogramma bidimensionale
mask = np.where(gas_mass > 0.307)[0]    #Individuazione dei 5 aloni per gli istogrammi
gas_mass6 = gas_mass[mask]
posx6 = posx[mask]
posy6 = posy[mask]
posz6 = posz[mask]
distance6 = [[] for i in range(len(gas_mass6))]

for i in range(len(gas_mass6)):
    distance6[i] = np.sqrt(np.square(posx-posx[i]) + np.square(posy - posy[i]) + np.square(posz - posz[i]))
    #Calcolo delle distanze delle altre strutture da questi aloni

nbins = 50
largdist = np.amax(distance6)/nbins                                    #Generazione bins dell'istogramma
largmass = (max(np.log10(total_mass))-min(np.log10(total_mass)))/nbins
binsdist = np.zeros(nbins + 1)
binsmass = np.zeros(nbins + 1)
for i in range(len(binsdist)):
    binsdist[i] = i*largdist
    binsmass[i] = min(np.log10(total_mass)) + i*largmass

for i in range(len(gas_mass6)): #Generazione degli istogrammi per i singoli aloni    
    istbid(np.log10(total_mass),distance6[i],binsmass,binsdist,'dell\'alone con massa di gas {} x 10^10 Msun/h'.format(gas_mass6[i]),'ist_bid_alone_{}.png'.format(i+1))

masstot = np.repeat(np.log10(total_mass),5)
disttot = np.concatenate((distance6[0],distance6[1],distance6[2],distance6[3],distance6[4]))
istbid(masstot,disttot,binsmass,binsdist,'totale','ist_bid_totale.png') #Istogramma totale
