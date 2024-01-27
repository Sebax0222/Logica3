#Se define la funcion y se le asigna un argumento
def contar_palabras_en_archivo(nombre_archivo): ##Se agregaron los dos puntos al final
    #Se genera un ciclo try para buscar abrir un archivo, leerlo y contar las palabras y posteriormente cerrarlo
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)
    #Se realiza una excepcion para retornar cuando no se encuentre el archivo.    
    except FileNotFoundError:
        return (f"El archivo {nombre_archivo} no fue encontrado.")##Se corrige la palabra return y se agregan los parentesis


#Se crea la variable para solicitar al usuario el nombre del archivo
nombre_archivo= input("Ingrese el nombre del archivo de texto: ")
#Se imprimen una texto y se llama a la funcion.
print(f"El archivo contiene {contar_palabras_en_archivo(nombre_archivo)} palabras.")
