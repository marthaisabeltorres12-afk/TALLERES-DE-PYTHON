# Pedir datos
promedio = float(input("Ingrese el promedio del alumno: "))
pension = float(input("Ingrese el valor de la pensión: "))

# cuanto debe pagar
if promedio >= 4.0:
    pagar = pension * 0.70
else:
    pagar = pension * 1.10   # incluye IVA del 10%

print("Valor a pagar por el alumno:", pagar)
