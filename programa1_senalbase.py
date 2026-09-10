### Los programas presentados aqui estan orientados a corrimiento de tiempo de 
# senales
import numpy as np 
import matplotlib.pyplot as plt 

## Rango de tiempo 
n =  np.arange(-20,21)
x = np.sin(0.2*np.pi*n)

# Graficar senal original 
plt.stem(n,x,basefmt=" ")
plt.title("Senal original x[n]")
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.show()

### 
