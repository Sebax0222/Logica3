def contar_palabra(texto, palabra):#Se agregan los dos puntos 
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.") #Se agrega } en palabra_buscada y se agrega { en el inicio de contar_palabra
