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

def plot_con_fit(x,y,xfit,yfit,nomex,nomey,udmx,udmy,scalax,scalay,marker,colore,colorefit,nomefigura):
    '''
    Questa funzione permette di produrre un grafico in base alle informazioni date come parametri
    ---------------------------------------------------------------------------------------------
    Parametri:
    x: Array di dati da graficare sull'asse delle x
    y: Array di dati da graficare sull'asse delle y
    xfit: Array dei dati dell'asse x del fit lineare
    yfit: Array di dati dell'asse y fit lineare
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
    ax.plot(xfit,yfit,color='{}'.format(colorefit))
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

baryonic_mass = gas_mass + stellar_mass
mask = np.where(baryonic_mass != 0.0)
barmass_fit = baryonic_mass[mask]
dmmass_fit = dm_mass[mask]
mask = np.where(dmmass_fit != 0.0)
barmass_fit = barmass_fit[mask]
dmmass_fit = dmmass_fit[mask]

barmass_fit = np.log10(barmass_fit)
dmmass_fit = np.log10(dmmass_fit)
mdm,qdm = np.polyfit(barmass_fit,dmmass_fit,1)
ydm= mdm*barmass_fit + qdm
barmass_fit = 10**(barmass_fit)
ydm = 10**(ydm)

plot_con_fit(baryonic_mass,dm_mass,barmass_fit,ydm,'Massa barionica','Massa di materia oscura','10^10 Msun/h','10^10 Msun/h','log','log','x','r','b','FiguraDM_MassaBarionica_fitlineare.png')

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

#QUARTO PUNTO: Distribuzione proiettata degli aloni

gas_mass1 = np.where(gas_mass == 0.0, 10**(-5), gas_mass)
stellar_mass1 = np.where(stellar_mass == 0.0, 10**(-5), stellar_mass)
gasutile = np.log10(gas_mass1) + 5.0
stellarutile = np.log10(stellar_mass1) + 5.0
cmap = plt.get_cmap('viridis')
norm = plt.Normalize(gasutile.min(), gasutile.max())
line_colors = cmap(norm(gasutile))
sizes = np.square(stellarutile)
subplot(posx,posy,posz,sizes,line_colors)

#QUINTO PUNTO: Grafico della massa del buco nero corrispondente alla struttura, in funzione della massa stellare

mask = np.where(bh_mass > 8.0*10**(-5))
bhmass_fit = bh_mass[mask]
stellarmass_fit = stellar_mass[mask]

bhmass_fit = np.where(stellarmass_fit == 0.0,bhmass_fit[0],bhmass_fit)
stellarmass_fit = np.where(stellarmass_fit == 0.0,stellarmass_fit[0],stellarmass_fit)

stellarmass_fit = np.log10(stellarmass_fit)
bhmass_fit = np.log10(bhmass_fit)

mbh,qbh = np.polyfit(stellarmass_fit,bhmass_fit,1)
ybh = mbh*stellarmass_fit + qbh
stellarmass_fit = 10**(stellarmass_fit)
ybh = 10**(ybh)

plot_con_fit(stellar_mass,bh_mass,stellarmass_fit,ybh,'Massa stellare','Massa del buco nero','10^10 Msun/h','10^10 Msun/h','log','log','.','b','r','FiguraBH_Massastellare.png')
