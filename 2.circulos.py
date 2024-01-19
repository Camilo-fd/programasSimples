import math
print("Ingrese el radio del circulo:\n")
radio = int(input())

perimetro = round(2 * (math.pi) * radio,2)

area = round(math.pi * radio**2,2)

print(f"El perimetro es: {perimetro}")
print(f"La area es: {area}")
