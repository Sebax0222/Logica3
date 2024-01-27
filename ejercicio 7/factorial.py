#Se define la funcion factorial con n como argumento
def factorial(n):##Se agregan los dos puntos
    #SE realiza un condicional para verificar que el argumento cumpla la condicion ser igual a 0 o 1 y retornar un 1 para esos casos
    if n == 0 or n == 1: ##Se agrega = para completar la comparacion y se agregan los dos puntos finales
        return 1 ##Se escribe correctamente el return
    else:
        #Se evidencia una funcion recursiva ya que se llama asi misma con el fin  de ir disminuyendo desde el numero dado hasta 1, para poder realizar el factorial
        return n * factorial(n - 1) ##Se escribe correctamente el return

#Se solicita al usuario ingresar un numero entero
numero = int(input("Ingrese un número para calcular su factorial: "))
#Se imprime el numero con el resultado de la funciona
print(f"El factorial de {numero} es {factorial(numero)}") ##Se agrega el argumento de la funcion llamada
