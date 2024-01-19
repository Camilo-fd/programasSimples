notas = []
suma = 0
n = int(input("Ingrese la cantidad de numeros: \n"))
for i in range(n):
    notas.append(float(input(f"Ingrese la nota: {i + 1}: \n")))
    
for i in range(len(notas)):
    suma += notas[i]

print(f"El promedio de numero es: {suma/n}")