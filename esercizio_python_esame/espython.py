import numpy as np
import matplotlib.pyplot as plt

data_filename = '/home/pietromg/esame/Esame_di_AIT/esercizio_python_esame/file2_Groups_AGN-wWU_500Mpc_Data.txt'
data = np.loadtxt(data_filename, unpack = True)
dm_mass = data[2]       #Massa di materia oscura. Misurata in 10^10 Msun/h
gas_mass = data[1]      #Massa di gas. Misurata in 10^10 Msun/h
stellar_mass = data[3]  #Massa di stelle. Misurata in 10^10 Msun/h

baryonic_mass = gas_mass + stellar_mass

fig, ax = plt.subplots()
fig.set_size_inches(18,10)
ax.set_title('Grafico della massa dell\'alone di materia oscura in funzione della massa barionica', fontsize=20)
ax.set_xlabel('Massa barionica [10^10 Msun/h]', fontsize=15)
ax.set_ylabel('Massa di materia oscura [10^10 Msun/h]', fontsize=15)
ax.set_xscale('log')
ax.set_yscale('log')
ax.scatter(baryonic_mass, dm_mass, marker='x', color='r')
ax.tick_params(axis='both', right=True, top=True, direction='in')
fig.savefig("figuraDM_vs_baryonic.png")

