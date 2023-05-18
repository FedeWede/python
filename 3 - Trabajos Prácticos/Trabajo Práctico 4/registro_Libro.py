class Libro:
    def __init__(self, titulo, cant_rev, anio, idioma, rating, isbn):
        self.titulo = titulo
        self.cant_rev = int(cant_rev)
        self.anio = int(anio)
        self.idioma = int(idioma)
        self.rating = float(rating)
        self.isbn = isbn

    def __str__(self):
        return f'Titulo: {self.titulo}|' \
               f'Revisiones: {self.cant_rev}|' \
               f'Año: {self.anio}|' \
               f'Idioma: {self.idioma}|' \
               f'Rating: {self.rating}|' \
               f'ISBN: {self.isbn}'
