
#pedir los datos de compra
cantidad= int(input("ingrese la cantidad de zapatillas"))
precio= int(input("ingrese el valor de cada zapatilla"))

#calcular la compra 
compra= cantidad * precio

#el descuento 
if cantidad >= 3:
    descuento = compra * 0.20
else:
    descuento= compra * 0.10

pagar = compra - descuento 

#resultado 
print("total de la compra", compra)
print("valor del descuento", descuento)
print(" total a pagar", pagar)