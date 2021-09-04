# a) Crear un vector 

Calificaciones = scan("https://raw.githubusercontent.com/VaneVarC/Ciencia-de-datos/master/Calificaciones.csv?token=AVKGPXIEY3QW7AV66KBRSVDBHRCC2", sep = ",", dec = ".")
#--------------------------------------------------------------------------------------------------------------

#b) ¿Cuántas notas contiene este vector? ¿Cuál es su valor medio?

Calificaciones = Calificaciones [!is.na(Calificaciones)]  #Para eliminar valores con NA
cat("Las Calificaciones son : ",Calificaciones)           #Se muestran las calificaciones
contador = length(Calificaciones)                         #Se cuenta cuantos elementos tiene el vector
cat("El vector tiene", contador, "notas")
promediar(Calificaciones, contador)                       #A la función promediar se le pasan los argumentos
#--------------------------------------------------------------------------------------------------------------

#c) Cambiar el 80 del vector anterior por un 8.0, sin volver a entrar el resto de notas. Volver a calcular la media de las notas tras haber corregido este error.

cat("\nCambiando el 80 por 8.0 ...")
Calificaciones[19]=8.0                                    #Cambio de valor 
cat("\nCambio realizado")
cat("\nLa lista corregida es:",Calificaciones, "\n")
promediar(Calificaciones, contador)                         
#--------------------------------------------------------------------------------------------------------------

#d) ¿Cuál es la nota mínima obtenida por estos estudiantes? ¿Cuántos estudiantes la han sacado?
 
Calif_baja = min (Calificaciones)                       
cat("\nLa calificacion más baja fue :", Calif_baja)       
x = which(Calificaciones == Calif_baja)                   #which busca los elementos que sean igual a la calificación baja
x1 = length(x)                                            #Cuenta cuantos elementos son y los asigna a la variable x
cat ("\nAlumnos que sacaron", Calif_baja,"son", x1, "se encuentran en las posiciones[", x, "]de la lista.")
#--------------------------------------------------------------------------------------------------------------

#e) ¿Cuántos estudiantes han logrado un notable (entre 7 y 8.9)? ¿Qué porcentaje del total de 
#estudiantes representan?

y = which(Calificaciones>=7 & Calificaciones<=8.9)        #Busca elementos entre 7 y 8.9 y los asigna al vector y
y1 = length(y)                                            
porcen = porcentaje(contador, y1)
cat("\nLos alumos que sacaron entre 7 y 8.9 son", y1, "que representan el", porcen, "% de la clase")
#--------------------------------------------------------------------------------------------------------------

#f)¿Qué grupo es más numeroso: el de los estudiantes que han sacado entre 4 y 4.9, o el de los que han sacado
#entre 5 y 5.9?

Calf_4 = which(Calificaciones>=4 & Calificaciones<=4.9)
Calf_5 = which(Calificaciones>=5 & Calificaciones<=5.9)
cat("¿Qué grupo es más numeroso: el de los estudiantes que han sacado entre 4 y 4.9, o el de los que han sacado entre 5 y 5.9?")
cat ("\nSe encontraro",length(Calf_4)," Calificaciones del 4 al 4.9")
cat ("\nSe encontraro",length(Calf_5)," Calificaciones del 5 al 5.9 ¿es mayor?: ", length(Calf_4)<length(Calf_5))
#--------------------------------------------------------------------------------------------------------------
cat("\nLa mediana es : ", Calcula_mediana(Calificaciones,contador))
cat("\nLa mediana con la funcion median es : ", median(Calificaciones))

#i) ¿Cuántos notas diferentes hay en esta muestra?
c = factor(Calificaciones)                                  #Se usa factor para sacar los niveles (calif. no repetidas)
c = length (levels(c))                                      #Al nivel se le saca la longitud 
cat("\nEn esta muestra hay", c, "notas diferentes.")