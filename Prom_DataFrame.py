import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/VaneVarC/Ciencia-de-datos/448609d9020d35e57f954e3bcb23b0425f22ef98/Materias%20(1).csv?token=AVKGPXKFVFNETLY7IAOAECDBHAT2C") #Cargado desde internet
#df = pd.read_csv("Materias (1).csv") //Cargado desde la computadora 
print("La lista es: \n", df)
suma = df["Calificaciones"].sum()
contador = df["Calificaciones"].count()
promedio = suma/contador
print(f"\n\n El promedio de las calificaciones es : {promedio}")
print("Presione [enter] para terminar el programa.")
input()
