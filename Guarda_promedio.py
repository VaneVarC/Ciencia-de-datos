import pickle as pk
numeros_a_prom = int(input("Cuantos números quieres promediar: "))
Guarda_num = list()
suma = 0
promedio = 0
for i in range(numeros_a_prom):
    num = int(input(f"Introduzca el {i + 1} ° número: "))
    Guarda_num.append(num)
    suma = suma + num
    promedio = suma / numeros_a_prom


print(f"El promedio de los {numeros_a_prom} : {promedio}")
print("Salvando la lista ...")
# filename
filename = "Salva_promedio.pkl"
# Crear y escribir el archivo
pk.dump(Guarda_num, open(filename, 'wb'))  # wb -> significa escribe
print("Salvado!")

respuesta = (input("¿Quieres ver los números que guardaste? si/no : "))
if respuesta == 'si':
    filename = 'Salva_promedio.pkl'
    loaded_data = pk.load(open(filename, 'rb'))  # rb -> lectura
    print(loaded_data)
else:
    if respuesta == 'no':
        print("Gracias por usar este programa")
