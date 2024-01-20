# def calculadora():
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == '+':
        resultado = num1 + num2
elif operacion == '-':
        resultado = num1 - num2
elif operacion == '*':
        resultado = num1 * num2
elif operacion == '/':
        resultado = num1 / num2
else:
     resultado = "Operación no válida"

print(f"Resultado: ", resultado)

# calculadora()
