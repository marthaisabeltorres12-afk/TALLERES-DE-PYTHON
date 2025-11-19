# Pedir cantidad
cantidad = int(input("Ingrese la cantidad de llantas: "))

#  precio por cantidad
if cantidad < 5:
    precio = 300000
elif cantidad <= 10:
    precio = 250000
else:
    precio = 200000

total = precio * cantidad

print("Precio por llanta:", precio)
print("Total a pagar:", total)
