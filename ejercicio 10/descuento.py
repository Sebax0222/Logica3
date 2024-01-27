#Se define la funcion y sus parametros
def calcular_precio_con_descuento(precio_base, porcentaje_descuento): ##Se agrega def y los puntos finales, se corrige la palabra descuento
    #Se define la variable descuento con la formula para el descuento
    descuento = precio_base * (porcentaje_descuento / 100)
    #Se define el precio final aplicando el descuento
    precio_final = precio_base - descuento
    return precio_final ##Se corrige la palabra return

#Se solicitan los datos al usuario
precio_base = float(input("Ingrese el precio base del producto: ")) ##Se agrega el input
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

#Se llama a la funcion para realizar el calculo y el porcentaje de descuento
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
#Se imprime el resultado del descuento segun el resultado de la funcion
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
