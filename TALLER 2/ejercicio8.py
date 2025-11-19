edad = float(input("Ingrese la edad en años (use 0.1 para meses): "))
sexo = input("Ingrese el sexo (m/f): ").lower()
hemo = float(input("Ingrese el nivel de hemoglobina: "))

# los rangos
if edad <= 1/12:
    minimo, maximo = 13, 26
elif edad <= 0.5:
    minimo, maximo = 10, 18
elif edad <= 1:
    minimo, maximo = 11, 15
elif edad <= 5:
    minimo, maximo = 11.5, 15
elif edad <= 10:
    minimo, maximo = 12.6, 15.5
elif edad <= 15:
    minimo, maximo = 13, 15.5
else:
    if sexo == "f":
        minimo, maximo = 12, 16
    else:
        minimo, maximo = 14, 18


if hemo < minimo:
    resultado = "Positivo (tiene anemia)"
else:
    resultado = "Negativo (no tiene anemia)"

print("Rango normal:", minimo, "-", maximo)
print("Resultado:", resultado)
