#Funciones
'''
Obejtivos

1. Legibilidad
2. Depuracion
3. Modificacion
4. Reutilizacion
5. Independencia


Anatomia


Desarrollo
Invocada



Ejemplo

'''

def pedir_numero(mensaje):
    numero = float(input(mensaje))

    return numero

def calcular_jubilacion(salario):
    nuevo_salario = salario - (salario * 0.10)

    return nuevo_salario

####################MAIN########################


salario = pedir_numero("Ingrese salario: ")
antiguedad = pedir_numero ("Ingrese antiguedad: ")

salario_con_descuento = calcular_jubilacion(salario)



print(f"El salario es: {salario}")
print(f"Su antiguedad es de: {antiguedad}")
print(f"Su salario con descuento es: {salario_con_descuento }")
