'''Escribir un programa que permita leer la can dad de números enteros ingresados por el usuario
y calcular lo siguiente:
El segundo menor
El promedio de los números posi vos.
El mayor de los números nega vos.'''


#Entradas
n = int(input('Ingrese la cantidad de números a procesar:'))
cont_positivos= 0
menor = None
segundo_menor =None
mayor_negativo = 0



for i in range(n):
    numero= int(input('Ingrese el número:'))       #Guardamos el numero numero
    if numero >=0 :
        cont_positivos += 1
    if numero < 0:
        if mayor_negativo > numero:
            mayor_negativo = numero
    if i ==0:
        menor = numero
    if i == 1:
        if menor < numero:
            segundo_menor= numero
        elif menor > numero:
            segundo_menor = menor
            menor = numero
    elif i>1:
        if menor > numero:
            segundo_menor = menor
            menor = numero
        elif segundo_menor > numero:
            segundo_menor = numero


print('El segundo menor es:', segundo_menor)

promedio = n / cont_positivos

print('el promedio de los numeros positivos:' , promedio)

if mayor_negativo != 0:
    print('El mayor negativo ingresado es de:', mayor_negativo)