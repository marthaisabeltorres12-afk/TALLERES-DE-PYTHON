 # Pedir el salario básico al usuario
salarioBasico = int(input("Ingrese el salario basico: "))

# Calcular la retención (18%)
retencion = salarioBasico * 0.18

# Calcular la bonificación (1.3%)
bonificacion = salarioBasico * 0.013

# Calcular el salario neto
salarioNeto = salarioBasico - retencion + bonificacion

print(f"Salario básico: {salarioBasico}")
print(f"Retención (18%): {retencion}")
print(f"Bonificación (1.3%): {bonificacion}")
print(f"Salario neto: {salarioNeto}")