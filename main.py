import os
os.system("cls")
from functions import *

print("""
==============================

    calculadora de gastos

==============================
""")


gasto1 = float(input("Ingrese el primer gasto\n"))
gasto2 = float(input("Ingrese el segundo gasto\n"))
gasto3 = float(input("Ingrese el tercer gasto\n"))

total = calcular_total(gasto1, gasto2, gasto3)
promedio = calcular_promedio(total, 3)
clasificacion = clasificar_gasto(total)

print()
print("================================")
print()
print("          RESULTADOS")
print()
print("================================")
print(f"total de gastos: ${total:.0f}")
print(f"Promedio de gastos: ${promedio:.2f}")
print(f"Clasificacion: {clasificacion}")
