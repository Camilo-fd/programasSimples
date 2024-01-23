Algoritmo sin_titulo
	Escribir "Ingrese el numero"
	Leer n
	Para i <- 1 Hasta Longitud(n) Con Paso 1 Hacer
		inverso = Concatenar(SubCadena(n,i,i),inverso)
	Fin Para
	Escribir inverso
FinAlgoritmo
