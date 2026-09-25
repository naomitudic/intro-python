# Añade una colección de libros

library = [
    {'title': 'Don Quijote de la Mancha', 'author': 'Miguel de Cervantes'},
    {'title': 'Anna Karenina', 'author': 'León Tólstoi'},
    {'title': 'Orgullo y Prejuicio', 'author': 'Jane Austen'},
    {"title": "La Galatea", "author": "Miguel de Cervantes"},
    {'title': 'Cien años de soledad', 'author': 'Gabriel García Márquez'},
    {'title': 'Emma', 'author': 'Jane Austen'},
    {'title': 'Cumbres Borrascosas', 'author': 'Emily Brontë'},
    {"title": "1984", "author": "George Orwell"},
    {'title': 'Frankenstein', 'author': 'Mary Shelley'},
    {"title": "El amor en los tiempos del cólera", "author": "Gabriel García Márquez"},
    {'title': 'La Regenta', 'author': 'Leopoldo Alas, Clarín'},
    {'title': 'La Celestina', 'author': 'Fernando de Rojas'},
    {'title': 'Sentido y Sensibilidad', 'author': 'Jane Austen'},
    {'title': 'Jane Eyre', 'author': 'Charlotte Brontë'},
    {'title': 'Crónica de una muerte anunciada', 'author': 'Gabriel García Márquez'},
    {'title': 'Asesinato en el Orient Express', 'author': 'Agatha Christie'},
    ]

# Muestra la colección de libros creada

print(library)

# Busca un libro por el autor

def books_by_author(books, author):
    titles = []
    for book in books:
        if book["author"].lower() == author.lower():
            titles.append(book["title"])
    return titles

print(books_by_author(library, "Jane Austen"))
print(books_by_author(library, "gabriel garcía márquez"))

# Verifica si un libro está disponible

def book_exists(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            return True
    return False

print(book_exists(library, "1984"))
print(book_exists(library, "El Quijote"))