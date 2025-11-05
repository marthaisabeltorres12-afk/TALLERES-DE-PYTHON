# Solicitar área total
area_total = float(input("Ingrese el área total del terreno (m²): "))

# Calcular distribuciones
cultivos = area_total * 0.40
vivienda = area_total * 0.25
zonas_verdes = area_total * 0.15
otros = area_total - (cultivos + vivienda + zonas_verdes)

# Mostrar resultados
print(f"Cultivos: {cultivos} m²")
print(f"Vivienda: {vivienda} m²")
print(f"Zonas verdes: {zonas_verdes} m²")
print(f"Área disponible: {otros} m²")
