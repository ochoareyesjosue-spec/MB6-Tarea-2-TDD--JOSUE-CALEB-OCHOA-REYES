def contar_palabras(texto):
    palabras = texto.split()  
    return len(palabras)
    
    
print(contar_palabras("hola mundo"))      # 2
print(contar_palabras(""))                # 0
print(contar_palabras("   hola   mundo")) # 2
print(contar_palabras("solo"))            # 1