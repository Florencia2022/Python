'''Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular
los siguientes puntos:
Determinar la cantidad de letras que tiene la palabra
Mostrar un mensaje que informe si la palabra termina en vocal
'''
#Entradas y/o datos
palabra= input('Ingrese la palabra a procesar: ')

#Procesos

#nos quedamos con el largo menos 1 para saber la cantidad de caracteres
cantidad = len(palabra)

#verificamos si el ultimo caracter es una vocal, si lo es prendemos la bandera
flag = False
vocal = 'AEIOUaeiou'
if palabra[cantidad-1] in vocal:
    flag = True

print('La cantidad de letras que tiene es de: ', cantidad)
if flag:
    print('La palabra termina en vocal!')