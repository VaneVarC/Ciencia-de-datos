numeros_a_prom = int(input("Cuantos números quieres promediar: "))
suma = 0
promedio = 0
for i in range(numeros_a_prom):
    num = int(input(f"Introduzca el {i + 1} ° número: "))
    suma = suma + num
    promedio = suma / numeros_a_prom


print(f"El promedio de los {numeros_a_prom} : {promedio}")
print("Presione [enter] para terminar el programa.")
input()
