"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecución y la lógica de un algoritmo.
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""

letter = input("Escribe un letra: ").lower()

if len(letter)==1 and letter.isalpha():
    if letter in "aeiouáéíóú":
        print("La letra es una vocal")
    else:
        print("La letra es consonante")

else:
    print("Por favor, ingresa una letra válida")

"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""

number = float(input("Ingresa una nota (de 0 a 100): "))

if 0 <= number <= 100:
    if number >= 90:
        grade = "A"
    elif number >= 80:
        grade = "B"
    elif number >= 70:
        grade = "C"
    elif number >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Tu calificación es: {grade}")

else:
    print("La nota ingresada está fuera del rango permitido.")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""

number = int(input("Ingresa un número: "))

if number > 0:
    while number >= 1:
        print(number)
        number -= 1

else:
    print("El número debe ser mayor que 0.")

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
text = input("Escribe aquí: ")

for letter in text:
    print(letter)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
words = []
uppercase_words = []

for i in range(5):
    word = input(f"Ingresa la palabra número {i+1}: ")
    words.append(word)

for word in words:
    uppercase_words.append(word.upper())

print("\nPalabras:", words)
print("Palabras en mayúsculas", uppercase_words)


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
pet = input("¿Cuál es tu mascota?: ").strip().lower()

if pet == "perro" or pet == "Perro":
    print("Tengo un perro.")
elif pet == "gato" or pet == "Gato":
    print("Tengo un gato")
elif pet == "pájaro" or pet == "Pájaro" or pet == "pajaro" or pet == "Pajaro":
    print("Tengo un pájaro")
else:
    print("No tengo una mascota convencional")