# Crear listas vacías
aprendices = []
edades = []

# Llenar listas solicitando datos por teclado
cantidad = int(input("¿Cuantos aprendices quiere ingresar?: "))

for i in range(cantidad):
    nombre = input("Nombre del aprendiz: ")
    edad = int(input("Edad del aprendiz: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir listas
print(f"Lista de aprendices: {aprendices}")
print(f"Lista de edades: {edades}")

# Mostrar el aprendiz con la mayor edad
mayorEdad = max(edades)
posicion = edades.index(mayorEdad)
print(f"El aprendiz con mayor edad es: {aprendices[posicion]} con {mayorEdad} años")

# Insertar nombre de la instructora en la posición 1
instructora = "Instructora"
aprendices.insert(1, instructora)
print(f"Lista despues de insertar instructora: {aprendices}")

# Contar cuantos aprendices tienen 18 años
cantidad18 = edades.count(18)
print(f"Aprendices con 18 años: {cantidad18}")

# Agregar un aprendiz “x” al final de la lista
aprendices.append("Gabriel")
print(f"Lista después de agregar Gabriel: {aprendices}")

# Borrar el nombre de la instructora
aprendices.remove(instructora)
print(f"Lista despues de borrar instructora: {aprendices}")

# Buscar un dato en la lista
buscar = input("Ingrese un nombre a buscar en la lista: ")
if buscar in aprendices:
    print(buscar, "Si esta en la lista")
else:
    print(buscar, "No esta en la lista")

# Mostrar los primeros 10 aprendices
print(f"Primeros 10 aprendices: {aprendices[:10]}")

# Mostrar los ultimos 10 aprendices
print(f"Últimos 10 aprendices: {aprendices[-10:]}")

# Mostrar del elemento 10 al 20
print(f"Del elemento 10 al 20: {aprendices[10:21]}")

# Mostrar elementos con indice par
print("Elementos con indice par:")
for i in range(0, len(aprendices), 2):
    print("Indice {i}: {aprendices[i]}")
