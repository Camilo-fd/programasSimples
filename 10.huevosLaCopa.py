import math
TH = float(input("Temperatura del huevo: "))
TE = 100 # temperatura de ebullicion del agua 
M = 47 #masa del huevo
p = 1.038 #ensidad
c = 3.7 #capacidad calorífica específica
k = 0.0054 #conductividad térmica

dividiendo = math.pow(M, (2/3)) * (c * (math.pow(p, (1/3)))) 
divisor = (k * (math.pow(math.pi, 2)) * (math.pow(4 * math.pi/3, (2/3))))
resultado = dividiendo / divisor
resultado2 = math.long(0.76 * (((TH - TE)) / (70 - TE)))
segundos = (resultado * resultado2)
minutos = round((segundos / 60))

print(f"EL tiempo maximo para preparar a la copa {round(segundos)}segundo")
print(f"EL tiempo maximo para preparar a la copa {minutos}minutos")

