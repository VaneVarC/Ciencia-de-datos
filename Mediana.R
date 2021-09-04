#g) Ordenad en orden creciente estas notas y obtened su mediana: una vez ordenado el vector,
#si tiene un número impar de entradas, su mediana es el valor central, y si tiene un número
#par de entradas, su mediana es la media aritmética de los dos valores centrales.
Calcula_mediana <- function(Vect, cont)
{
  Vect = sort(Vect)
  elemento = cont/2
  if (cont %% 2 == 0) # Si las entradas son par
  {
    mediana = (Vect[elemento]+ Vect[elemento + 1 ]) / 2
    return(mediana)
  }
  else  #Si las entradas son impar
  {
    mediana = Vect[elemento]
    return(mediana)
  }
}