import pandas as pd

df = pd.read_csv("Materias (1).csv")
print("La lista es: \n", df)
suma = df["Calificaciones"].sum()
contador = df["Calificaciones"].count()
promedio = suma/contador
print(f"\n\n El promedio de las calificaciones es : {promedio}")
print("Presione [enter] para terminar el programa.")
input()
