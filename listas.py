from os import system

nombres=[]
apellidos=[]

nombres.append("Álvaro")
nombres.append("Wacoldo")
nombres.append("Amada")

apellidos.append("Gatica")
apellidos.append("Soto")
apellidos.append(input("Ingrese apellido: "))

print(nombres)
print(apellidos)

for i in range(len(nombres)):
    n=i+1
    print(f"Persona {n}: {nombres[i]} {apellidos[i]}")
