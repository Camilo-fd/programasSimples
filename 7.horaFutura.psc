Algoritmo sin_titulo
	Definir ha , horas Como Real
	Definir cant Como Entero
	Escribir "Ingresa la hora actual"
	Leer ha
	Escribir "Cantidad de horas"
	Leer cant
	horas = (cant + ha) % 24
	Escribir "En ", cant, " el reloj marcara las ", ha, " horas"
FinAlgoritmo
