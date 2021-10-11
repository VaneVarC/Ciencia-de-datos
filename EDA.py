#***********************************
#*   IMPORTACION DE LIBRERIAS      *
#***********************************
import pandas as pd
import numpy as np
import seaborn as sns #Libreria que sirve para hacer graficas
import matplotlib.pyplot as plt #Libreria para graficas
#%matplotlib inline   # <- se omite porque solo es para notebook como Colab o jupyter
sns.set(color_codes=True) # para los colores.

#************************************************
#* Cargar el dataFrame y ver los tipos de datos *
#************************************************
#df=pd.read_csv("data.csv")   #Se carga desde la computadora.
df=pd.read_csv("https://raw.githubusercontent.com/VaneVarC/Ciencia-de-datos/master/data.csv?token=AVKGPXM6OQMN4YELI7P2DDLBNTTEG")  #Se carga desde internet
print("Se muestra el encabezado del DataFrame\n")
print(df.head(5))
print("\nSe muestran los 5 últimos renglones del DataFrame\n")
print(df.tail(5))
print("\n Tipo de datos\n")
print(df.dtypes)

#*************************************
#*  Descartar columnas irrelevantes  *
#*************************************
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors','Vehicle Size'], axis=1)
#axis=1 elimina las columnas, axis=0 elimina renglones, equivale a df.drop(columns=['..','...'])
print("\nSe eliminaron las columnas 'Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity'")
print("'Number of Doors', 'Vehicle Size'  porque son columnas irrelevantes para este análisis\n")
print(df.head(5))

#*******************************
#*    Renombrar las columnas   *
#*******************************
df = df.rename(columns={'Engine HP': 'HP', 'Engine Cylinders':'Cylinders', 'Transmission Type': 'Transmission', 'Driven_Wheels':'Drive Mode','highway MPG': 'MPG-H', 'city mpg': 'MPG-C', 'MSRP': 'Price'})
print("Se reenombraron las columnas\n")
print(df.head(5))

#*************************************
#*  Descartar renglones duplicados   *
#*************************************
print("\nNúmero total de renglones y columnas :", df.shape)
duplicate_rows_df = df[df.duplicated()]
print("Número de renglones duplicados: ", duplicate_rows_df.shape)
print("Número de filas antes de eliminar\n", df.count())
#Eliminación de los duplicados
df = df.drop_duplicates()
print("\nSe eliminaron los duplicados\n",df.head(5))
print("\nNúmero de filas después de eliminar\n", df.count())

#****************************************************
#*   Descartar los valores faltantes o nulos        *
#* En éste caso se puede hacer porque hay poquitos  *
#* valores faltantes.                               *
#****************************************************
print("\nEncontrando valores nulos:\n", df.isnull().sum())
#Eliminacion de valores nulos
df = df.dropna()
print("\nBorrando los valores perdidos\n", df.count ())
print("\nAhora los valores nulos son:\n",df.isnull().sum())

#*********************************************
#*   Deteccion de valores atípicos,          *
#*   para tener un modelo más preciso,       *
#*   mediante la Técnica de puntuación IQR   *
#*********************************************
sns.boxplot(x=df['Price'])
plt.show()  #mostrar el grafico
sns.boxplot(x=df['Cylinders'])
plt.show() #mostrar el grafico
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("\nResumen de valores del quartil 3 - quartil 1\n",IQR)
df = df[~((df < (Q1-1.5 * IQR))|(df > (Q3 + 1.5 * IQR))).any(axis = 1)]
print(df.shape)

#********************************************
#*  Gráficas de dispersión e histograma   *
#********************************************
#Para saber el número de carros manufacturado por una empresa diferente, con gráfica de histograma
df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Número de carros por marca")
plt.ylabel("Número de carros")
plt.xlabel("Marca")
plt.show() #Muestra el histograma
#Para encontrar relaciones entre variables con mapas de calor
plt.figure(figsize=(20,10))  #figzice -> tamaño de la gráfica
c = df.corr()
sns.heatmap(c, cmap="BrBG", annot=True)
print("La función de precio depende del tamaño del motor, caballos de fuerza,")
print("y los cilindros\n",c)
plt.show()  #Muestra el mapa de calor

#***********************************
#*    Diagrama de dispersión       *
#***********************************
fig, ax = plt.subplots(figsize = (10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Precio')
plt.show()
