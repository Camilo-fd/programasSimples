print("Escribe acontinuacion los certamnes y el laboratorio")
c1 = int(input("Nota certamen 1: "))
c2 = int(input("Nota certamen 2: "))
c3 = 0
lab = int(input("Nota Laboratorio: "))
Nl = lab
Nc = int((c1 + c2) / 2)
Nf =  float(round((60 - (Nc * 0.7 + Nl * 0.3)) / 0.7,2))
print(f"Necesita nota {Nf} en el certamen 3")