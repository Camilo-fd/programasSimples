print("-----------------------------")
hora_actual = float(input("Hora actual:\n"))
cantidad_horas = int(input("Cantidad de horas:\n")) 
horas = float((cantidad_horas + hora_actual)) % 24
print(f"En {cantidad_horas}, el reloj marcara las {round(horas,2)} horas")
print("-----------------------------")