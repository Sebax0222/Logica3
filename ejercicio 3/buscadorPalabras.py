#Se define la funcion contar palabra donde se pone como parametros las variables texto y palabra
def contar_palabra(texto, palabra):##Se agregan los dos puntos 
    #se usan los metodos .lower para poner todas las palabras en minusculas, el metodo .split para separar las letras, y .count para contas las palaras repetidas
    return texto.lower().split().count(palabra.lower())

#Se define la variable texto con un string con multiples palabas repetidas
texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
#Se define la variables palabra buscada con el string a buscar en la funcion.
palabra_buscada = "texto"

#Se imprime con f strings (una forma de concatenar textos y variables), se pone la pabra buscada,
# y luego se llama a la funcion para al final imprimir el mensaje con las veces que se conto la palabra
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.") ##Se agrega } en palabra_buscada y se agrega { en el inicio de contar_palabra
