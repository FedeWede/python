class Libros:
    def __init__(self, codigo, titulo, genero, idioma, precio):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio

    def __str__(self):
        return f'Codigo: {self.codigo} |' \
               f'Título: {self.titulo} |' \
               f'Genero: {self.genero} |' \
               f'Idioma: {self.idioma} |' \
               f'Precio: ${self.precio}'
