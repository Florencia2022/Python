'''Realizar un programa que genere 15 numero aleatorios enteros en el rango del 1 al 100, que representaria la 
tarjeta de bingo de una persona. Una vez generado los numeros aleatorios solicitar al
usuario que ingrese 3 numeros enteros, a partir de alli mostrar los siguientes mensajes:
Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador tiene mala suerte,
no marco ninguna casilla”.
Caso contrario mostrar “El jugador marco algun numero de la tarjeta”'''
import random

#Entradas y/o datos

tarjeta_bingo = random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100),random.randint(1,100), random.randint(1,100)

#guardar los numeros del usuario
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))

#Verifico si alguno esta en la tarjeta bingo
if num1 in tarjeta_bingo or num2 in tarjeta_bingo or num3 in tarjeta_bingo:
    print("gano")
else:
    print("El jugador tiene mala suerte, no marco ninguna casilla")

print(tarjeta_bingo)