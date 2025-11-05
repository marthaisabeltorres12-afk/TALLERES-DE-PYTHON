# Solicitar área total
areaTotal = float(input("Ingrese el área total del terreno (m²): "))

# Calcular distribuciones
cultivos = areaTotal * 0.40
vivienda = areaTotal * 0.25
zonasVerdes = areaTotal * 0.15
otros = areaTotal - (cultivos + vivienda + zonasVerdes)

# Mostrar resultados
print(f"Cultivos: {cultivos} m²")
print(f"Vivienda: {vivienda} m²")
print(f"Zonas verdes: {zonasVerdes} m²")
print(f"Área disponible: {otros} m²")
