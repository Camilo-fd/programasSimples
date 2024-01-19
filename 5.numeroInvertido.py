n = input("Ingrese el numero: ")
inverso = ""
for i in range(len(n)):
    inverso += n[-(i+1)]
print(inverso)