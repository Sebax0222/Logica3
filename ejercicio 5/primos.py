# Se define la funcion es primo
def es_primo(numero): ##Se agregan los dos puntos
    #Se condiciona que en caso de que le variable sea menor a 2 retorne un falso
    if numero < 2: ##Se agregan los dos puntos
        return False
    # Se realiza un ciclo for que recorre un rango  desde el 2 hasta la raiz cuadrada de numero + 1 para incluir el numero en el rango
    for i in range(2, int(numero**0.5) + 1):##Se agregan los dos puntos
        if numero % i == 0:##Se agregan los dos puntos
            return False ##Se corrige la palabra return
    return True ##Se corrige la palabra return

#Se define la variable limite y se le consulta al usuario
limite = int(input("Ingrese el límite superior para encontrar números primos: "))
#Se define la variable primo la vual es definida como una lista donde se itera en el rango defindo por el usuario y saca los numeros que coinciden con
#Los requisitos de la funcion y los guarda en una lista para imprimirlo posteriormente.
primos = [num for num in range(2, limite + 1) if es_primo(num)]##Se anade el argumento para completar la funcion
print("Números primos:", primos)
