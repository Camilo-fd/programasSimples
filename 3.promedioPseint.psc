Algoritmo sin_titulo
	Escribir "Ingrese la cantidad de numeros"
	Leer n
	acum = 0
	Para i<-1 Hasta n Con Paso 1 Hacer
		Escribir "Ingrese la cantidad de notas " i ":" 
		Leer notas
		acum = acum+notas
	Fin Para
	di = acum/n
	Escribir "promedio: ", di
FinProceso
 
