#                           programa4_sinusdesc.py 
# programa4_sinusdesc.py es un programa que muestra una grafica discreta de una senal seno decreciente 
##################################################################################################################

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
n = np.arange(0, 100)                  # Índice discreto
f = 0.05                               # Frecuencia (en ciclos/muestra)
amplitud = np.exp(-0.05 * n)          # Amplitud decreciente exponencialmente
senoidal = amplitud * np.sin(2 * np.pi * f * n)

# Graficar
plt.stem(n, senoidal, basefmt=" ")
plt.title('Señal Senoidal Discreta con Amplitud Decreciente')
plt.xlabel('n (muestras)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()
