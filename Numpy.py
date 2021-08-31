import numpy as np

Lista = np.array([1, 4, 0, 2, 7, 9, 0, 3, 0, 0, 8, 0, 5, 6])
print(Lista)
print("Índices en donde se encontró 0 son :")
indice = (np.where(Lista == 0)[0])  
print(indice+1)  # Los convierte en Base 1 para que sea más amigable con el usuario
