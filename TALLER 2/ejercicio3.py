# Pedir el monto total de la compra
monto = float(input("Ingrese el monto total de la compra: "))

#  Si excede de 500000
if monto > 500000:
    propio = monto * 0.55
    banco = monto * 0.30
    credito = monto * 0.15
    pagar = monto  
    print("Inversión propia: ", propio)
    print("Préstamo del banco: ", banco)
    print("Crédito al fabricante:", credito)
    print("Total a pagar:", pagar)

#  no excede de 500000
else:
    propio = monto * 0.70
    credito = monto * 0.30
    interes = credito * 0.20
    credito = credito + interes
    pagar = propio + credito
    
    # Resultados
    print("Inversión propia:", propio)
    print("Crédito al fabricante: ", credito)
    print("Interés del fabricante (20%): ", interes)
    print("Total a pagar al fabricante: ", credito)
    print("Total a pagar por la empresa: ",pagar)
