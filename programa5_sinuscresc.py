#                           programa5_sinuscresc.py
## programa5_sinuscresc.py es un programa que muestra una senal senoidal creciente  discreta 
##################################################################################################

import numpy as np 
import matplotlib.pyplot as plt 

## Parametros 
n = np.arange(0,100)
f = 0.05
amplitud = 1-np.exp(-0.05*n)
senoidal = amplitud*np.sin(2*np.pi*f*n)

## Graficar
plt.stem(n, senoidal)
plt.title("Senal senoidal discreta con amplitud creciente")
plt.xlabel("n (muestras)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()
