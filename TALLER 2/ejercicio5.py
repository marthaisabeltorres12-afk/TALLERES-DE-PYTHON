# Pedir datos
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (f/m): ").lower()

# Formula
if sexo == "f":
    pulsaciones = (220 - edad) / 10
else:
    pulsaciones = (210 - edad) / 10

print("Número de pulsaciones cada 10 segundos:", pulsaciones)
