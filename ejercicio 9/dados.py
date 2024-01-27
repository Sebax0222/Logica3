#Se importa la libreria random
import random ##Se corrige la palabra random

#Se define la funciona con sus argumentos
def simular_lanzamiento_dados(cantidad_dados, caras_por_dado): ##Se define la funcion agregando def
    #se define la variable resultados como una lista donde en el rango estipulado en los inputs se generan numeros aleatorios
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    #Se retorna la variable anterior
    return resultados ##Se corrige la palabra return

#Se definen las variables con las que se va a trabajar
cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
#Se llama a la funciona y se guarda el resultado en la variable lanzamientos la cual es impresa posteriormente
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado)##Se agrega el argumento faltante
print(f"Resultados del lanzamiento: {lanzamientos}")
