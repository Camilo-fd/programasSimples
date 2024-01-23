import math
print("Escribe acontinuacion los certamnes y el laboratorio")
c1 = int(input("Nota certamen 1: "))
c2 = int(input("Nota certamen 2: "))
lab = int(input("Nota Laboratorio: "))
Nl = lab
Nc = (59.6 - Nl * 0.3) / 0.7
c3 = 3 * Nc - c1 - c2 
print(f"Necesita nota {math.ceil(c3)} en el certamen 3")