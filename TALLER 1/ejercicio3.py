# Solicitar el valor inicial del desempleo
desempleoInicial = int(input("Ingrese el valor inicial del desempleo : "))

# Aumento del 9.5% en el primer trimestre
aumento = desempleoInicial * 0.095
desempleoDespuesAumento = desempleoInicial + aumento

# Caída del 1.5% en el segundo trimestre
disminucion = desempleoDespuesAumento * 0.015
desempleoActual = desempleoDespuesAumento - disminucion

print(f"Desempleo inicial: {desempleoInicial}")
print(f"Aumento (9.5%): +{aumento}")
print(f"Después del aumento: {desempleoDespuesAumento}")
print(f"Disminución (1.5%): -{disminucion}")
print(f"Desempleo actual: {desempleoActual}")