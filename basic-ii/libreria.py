"""
--------------------------- FUNCIONES ---------------------------
En este taller aprenderás a crear funciones en Python, desde las básicas hasta las que retornan valores, manejo de errores y excepciones, y su uso en clases.
"""


"""
--- Ejercicio 1: Función para Agregar Libros ---
Crea una función llamada `agregar_libro` que acepte dos parámetros, `titulo` y `autor`,
y que retorne un diccionario con el título y el autor del libro.
"""

def add_book(title, author):
    return{
        "title": title,
        "author": author,
    }

# Prueba la función con algunos valores

libro1 = add_book("Don Quijote de la Mancha", "Miguel de Cervantes")
libro2 = add_book("Cien años de soledad", "Gabriel García Márquez")
libro3 = add_book("1984", "George Orwell")

print(libro1)
print(libro2)
print(libro3)

print(libro1["title"], "-", libro1["author"])

"""
--- Ejercicio 2: Función para Listar Libros ---
Crea una función llamada `listar_libros` que acepte una lista de diccionarios `libros` y 
que retorne una lista con los títulos de los libros.
"""

def list_books(books):
    titles = []
    for book in books:
        titles.append(book["title"])
    return titles

# Prueba la función con algunos valores

books = [
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "George Orwell"},
]

print(list_books(books))

"""
--- Ejercicio 3: Función para Buscar Libros ---
Crea una función llamada `buscar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne el diccionario del libro que coincida con el título, o `None` si no se encuentra.
"""

# Escribe tu código aquí

def search_book(books, title):
    title = title.lower()
    for book in books:
        if title in book["title"].lower():
            return book
    return None

# Prueba la función con algunos valores

books = [
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "George Orwell"},
]

print(search_book(books, "don quijote de la mancha"))
print(search_book(books, "DON QUIJOTE"))
print(search_book(books, "Moby Dick"))

"""
--- Ejercicio 4: Manejo de Errores ---
Crea una función llamada `quitar_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que intente quitar el libro con el título especificado. Si no se encuentra el libro, maneja el error adecuadamente.
"""

def remove_book(books, title):
    try:
        removed_book = None
        for book in books:
            if book["title"].lower() == title.lower():
                removed_book = book
                break

        if removed_book is None:
            raise ValueError(f"Error: {title} no se encuentra disponible")

        books.remove(removed_book)
        print(f"{title} fue eliminado con éxito")
        return books

    except ValueError as error:
        print(f"Error: {error}")
        return None

# Prueba la función con algunos valores

books = [
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "George Orwell"},
]

result = remove_book(books, "don quijote de la mancha")
print(result)

"""
--- Ejercicio 5: Función que Retorna un Diccionario ---
Crea una función llamada `crear_inventario` que acepte una lista de diccionarios `libros` y 
que retorne un diccionario con la cantidad de libros por autor.
"""

def create_inventory(books):
    inventory = {}
    for book in books:
        author = book["author"]
        if author in inventory:
            inventory[author] += 1
        else:
            inventory[author] = 1
    return inventory

# Prueba la función con algunos valores

books = [
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "La Galatea", "author": "Miguel de Cervantes"},
    {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"title": "El amor en los tiempos del cólera", "author": "Gabriel García Márquez"},
    {"title": "Crónica de una muerte anunciada", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "George Orwell"},
]

print(create_inventory(books))

"""
--- Ejercicio 6: Función que Retorna una Lista ---
Crea una función llamada `libros_por_autor` que acepte una lista de diccionarios `libros` y un `autor` y 
que retorne una lista con los títulos de los libros escritos por el autor especificado.
"""

def books_by_author(books, author):
    author = author.lower()
    return [book["title"] for book in books if author in book ["author"].lower()]

# Prueba la función con algunos valores

books = [
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "La Galatea", "author": "Miguel de Cervantes"},
    {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"title": "El amor en los tiempos del cólera", "author": "Gabriel García Márquez"},
    {"title": "Crónica de una muerte anunciada", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "George Orwell"},
]

print(books_by_author(books, "gabriel garcía márquez"))
print(books_by_author(books, "CERVANTES"))
print(books_by_author(books, "Isabel Allende"))

"""
--- Ejercicio 7: Función que Retorna un Booleano ---
Crea una función llamada `existe_libro` que acepte una lista de diccionarios `libros` y un `titulo` y 
que retorne `True` si el libro existe en la lista, y `False` en caso contrario.
"""

def book_exists(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            return True
    return False

# Prueba la función con algunos valores

books = [
    {"title": "Don Quijote de la Mancha", "author": "Miguel de Cervantes"},
    {"title": "Cien años de soledad", "author": "Gabriel García Márquez"},
    {"title": "1984", "author": "Orwell"},
]

print(book_exists(books, "don quijote de la mancha"))
print(book_exists(books, "Don Quijote de la Mancha"))
print(book_exists(books, "Moby Dick"))