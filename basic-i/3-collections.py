"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""

pets = ['perro', 'gato', 'loro']
print(pets)

# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola

print(len(pets))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola

print(pets[2])

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista

pets.append('hamster')

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista

pets[1] = 'pez'
print(pets)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista

pets.remove('perro')
print(pets)

"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""

plantas = ('cactus', 'orquidea', 'rosas')

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola

print(len(plantas))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola

print(plantas[2])

# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede

# Escribe tu análisís acá acerca de qué sucede

# El resultado obtenido es "TypeError: 'tuple' object does not support item assignment", pues las tuplas no permiten modificación de nningún tipo tras su creación.

"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""

names = {'Maria', 'Cris', 'Cris', 'Alex'}
print(names)

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"

# El nombre de Cris se omite en vez de repetirse dos veces, porque los sets no admiten que se repita un mismo elemento. Además, el orden de los elementos es distinto pues no tiene por qué seguirse el orden preestablecido al definirlo, no existe ningún orded en los sets.

# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola

print(len(names))

# Escribe el código para acceder al valor de la posición 3, imprimir por consola

# print(names[3]); --> Este código siempre dará error a menos que añadamos un nombre que ocupe esa posición 3, pues solo hay tres nombres y el primero ocupa la posición 0.

# Escribe el código para agregar una elemento al set, imprimir por consola el set

names.add('Elena')
print(names)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set

names.remove('Maria')
print(names)

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""

city = {'name': 'Barcelona', 'country': 'Spain'}
print(city)

# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'

print(city['name'])

# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'

city.update({'population': '1700000'})
print(city)

# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola

city.update({'population': '1729963'})
print(city)

# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola

del city['country']
print(city)