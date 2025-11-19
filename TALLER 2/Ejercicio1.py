#solicitar las 3 calificaciones
nota1= int(input("ingrese su primera nota"))
nota2= int(input("ingrese su segunda nota"))
nota3= int(input("ingrese su tercera nota"))
#calcular el promedio
suma= nota1 + nota2 + nota3
promedio= suma/3
#el resultado
print(f"promedio {promedio:.2f} ")
if promedio >= 70:
    print(" aprobo algoritmia")
else:
    print("reprobo algoritmia")