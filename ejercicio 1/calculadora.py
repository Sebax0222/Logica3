#define la funcion calculadora
def calculadora():
    
 # La linea 2, 3 y 4 Definen 3 varias, 2 tipo numero y otra tipo string para definir los numeros a operar y la operacion
 
    num1 = float(input("Ingrese el primer número: ")) ##Se agrega los inputs en las variables num1 y 2
    num2 = float(input("Ingrese el segundo número: ")) ##Se agrega los inputs en las variables num1 y 2
    operacion = input("Ingrese la operación (+, -, *, /): ")

# Desde la linea 6 a la 15 hay un bloque de condicionales if, elif y else donde se definen las operaciones a realizar 
# segun los datos ingresados
    if operacion == '+':
        resultado = num1 + num2 ##Se corrige las variables num1 en los condicionales
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2 ##Se corrige las variables num1 en los condicionales
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = "Operación no válida"
        
# El return de devuelve el resultado de la operacion y el print imprime el resultado
    return print(resultado) ##se agrega el return un el print final y se elimina el texto por problemas de concatenacion

# Llamado de la funcion
calculadora() ##Se corrige la palabra calculadora








#
