
import numpy as np 
import matplotlib.pyplot as plt 

## Rango de tiempo 
n0 =  8     # Desplazamiento
n = np.arange(-20,21,0.5)
x = np.sin(0.2*np.pi*(n))
x_shifted = np.sin(0.2*np.pi*(n-n0))

### Graficar senal original 
plt.subplot(2,1,1)
plt.stem(n,x, basefmt= " ")
plt.title(f'Senal original: x[n]')
plt.xlabel('n')
plt.ylabel(f'x[n]')
plt.grid(True)


plt.subplot(2,1,2)
plt.stem(n,x_shifted, basefmt= " ")
plt.title(f'Senal desplazada: x[n-{n0}]')
plt.xlabel('n')
plt.ylabel(f'x[n-{n0}]')
plt.grid(True)

# Mostrar las graficas
plt.tight_layout()
plt.show()
