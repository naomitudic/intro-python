"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""

message = ("¡Hola, Mundo!")
print(message)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""

message = ("Hello world!")
print(message)

# Cuando introduces un nuevo valor para una misma variable el resultado que imprime el programa es este nuevo valor, sustituyendo al otro.

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""

# Variables
var_string = str("¡Hola, Mundo!")
var_int = int(3)
var_float = float(3)
var_bool = bool(True)
var_list = ["paper", "scissors", "pencil", "pen", "marker", "eraser", "notebook", "ruler"]
var_tuple = ("paper", "scissors", "pencil", "pen", "marker", "eraser", "notebook", "ruler")
var_dicctionary = {
    "song": "Billie Jean",
    "author": "Michael Jackson",
    "year": "1983",
}
var_set = {"paper", "scissors", "pencil", "pen", "marker", "eraser", "notebook", "ruler"}

# Impresión de las variables
print(var_string)
print(var_int)
print(var_float)
print(var_bool)
print(var_list)
print(var_tuple)
print(var_dicctionary)
print(var_set)

# Impresión del tipo de variable
print(type(var_string))
print(type(var_int))
print(type(var_float))
print(type(var_bool))
print(type(var_list))
print(type(var_tuple))
print(type(var_dicctionary))
print(type(var_set))
