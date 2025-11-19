# Pedir el valor de la compra
compra = float(input("Ingrese el valor de la compra: "))
color = input("Ingrese el color de la balota (rojo / verde / otro): ").lower()

# Determinar descuento
if color == "rojo":
    descuento = compra * 0.15
elif color == "verde":
    descuento = compra * 0.20
else:
    descuento = 0

valor_pagar = compra - descuento

print("Valor de la compra:", compra)
print("Color de la balota:", color)
print("Descuento aplicado:", descuento)
print("Valor a pagar:", valor_pagar)

