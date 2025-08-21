def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

print("Resultado:", contar_palabras("hola mundo"))