import random #Se completa la palambra ramdom
import string

def generar_contraseña(longitud=8):#Se define la funcion agregando def 
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña #Se escribe correctamente la palabra return

print(generar_contraseña()) #Se escribe correctamente la palabra contraseÑa
