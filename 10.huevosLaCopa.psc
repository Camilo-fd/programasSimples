Algoritmo sin_titulo
	Escribir "Temperatura del huevo"
	Leer TH 
	TE = 100
	M = 47
	p = 1.038
	c = 3.7
	k = 0.0054
	
	dividiendo = ((M^(2/3)) * (c * (p^(1/3))))
	divisor = ((k * PI^(2)) * (4 * PI/3)^(2/3))
	resultado = dividiendo / divisor
	resultado2 = ln(((0.76 * (TH - TE) / (70 - TE))))
	seg = resultado * resultado2
	minutos = redon(seg / 60)
	
	
	Escribir "El tiempo maximo para preparar a la copa ", trunc(seg) " segundos"
	Escribir "El tiempo maximo para preparar a la copa ", trunc(minutos) " segundos"
FinAlgoritmo
