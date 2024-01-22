Algoritmo circulos
	definir radio, perimetro, area Como Real
	Escribir "Ingrese el radio del circulo"
	Leer radio
	
	perimetro = trunc(2 * PI * radio)
	area = trunc(PI * radio^2)
	
	Escribir "El perimetro es: " , perimetro
	Escribir "La area es: " , area
	
FinAlgoritmo
