import numpy as np 
import matplotlib.pyplot as plt 

## Parametros de las senales a verificar 
n = np.arange(-20,21,0.2)
x =  np.sin(0.2*np.pi*n)

x_inverted = np.sin(0.2*np.pi*(-n))
## Graficar original 
plt.subplot(2,1,1)
plt.stem(n,x,basefmt=" ")
plt.title("Senal Original x[n]=sin(0.2*pi*n)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)

## Graficar senal invertida 
plt.subplot(2,1,2)
plt.stem(n,x_inverted, basefmt=" ")
plt.title("Senal Invertida x[-n]=sin(0.2*pi*(-n))")
plt.xlabel('n')
plt.ylabel('x[-n]')
plt.grid(True)

# Mostrar las graficas
plt.tight_layout()
plt.show() 
