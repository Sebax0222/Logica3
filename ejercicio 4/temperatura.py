#Se define la funciona celsius_a_fahrenheit y se pone como parametro la variable celsius
def celsius_a_fahrenheit(temperatura_celsius):##Se agregan los dos puntos finales
    #Se ejecuta la formula de conversion de grados fahrenheit a celsius
    return (temperatura_celsius * 9/5) + 32 ##Se agrega el + entre el parentesis y el 32 para completar la formula de conversion de grados  


#Se define la variable temperatura_celsius como un numero float
temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))##Se agrega el input para preguntar el numero a convertir
#Se define la variable temperatura_fahrenheit como el resultado de la ejecucion de la funcion usando como parametro la variable anterior 
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
#Se imprime en pantalla en modo string el resultado de la conversion realizada
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
