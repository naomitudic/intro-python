"""
--------------------------- OPERADORES ---------------------------
En este taller aprenderás usar los diferentes tipos de operadores
"""

"""
--- Ejercicio 1 operadores aritméticos  ---
Reemplaza el ? con el operador según sea el caso
"""
x = input("Ingresa el primer número: ")
y = input("Ingresa el segundo número: ")

num1 = int(x)
num2 = int(y)

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

"""
--- Ejercicio 2 operadores lógicos  ---
Reemplaza el ? con el operador según sea el caso
Puedes investigar sobre las tablas de la verdad, recuerda "las amigas de mis amigas, son mis amigas"
"""

michi_4_patas = True
michi_3_ojos = False
michi_vuela = False
michi_interesado = True
michi_juega = True
michi_pone_huevos = False

print(f"AND: {michi_4_patas and michi_3_ojos}")
print(f"OR: {michi_interesado or michi_vuela}")
print(f"NOT bool1: {not michi_juega}")
print(f"NOT bool2: {not michi_pone_huevos}")

"""
--- Ejercicio 3 Comparadores  ---
Reemplaza el ? con el comparador según sea el caso
"""

num3 = input("Ingresa el primer número: ")
num4 = input("Ingresa el segundo número: ")

a = int(num3)
b = int(num4)

print(f"¿a es igual a b?: {a == b}")
print(f"¿a es diferente de b?: {a != b}")
print(f"¿a es mayor que b?: {a > b}")
print(f"¿a es menor que b?: {a < b}")
print(f"¿a es mayor o igual que b?: {a >= b}")
print(f"¿a es menor o igual que b?: {a <= b}")