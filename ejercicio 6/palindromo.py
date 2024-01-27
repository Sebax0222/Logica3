
#Se define la funcion es_palindromo en la cual segun un suceso de instrucciones se convierte un texo en una cadena 
# en minuscula.
def es_palindromo(texto): ##Se agregan 2 puntos al final
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    #Se compara el texto inicial con el mismo a la inversa [::-1] para verificar si la palabra es un palindromo
    return texto == texto[::-1]

#Se solicita al usuario ungresar una palabra
palabra = input("Ingrese una palabra o frase: ")
#Con condicionales se llama a la funciona y se predeterminan mensajes segun sea true o false la respuesta de la funciona.
if es_palindromo(palabra): ##Se agrega el argumento segun la palabra anexa por el usuario.
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
