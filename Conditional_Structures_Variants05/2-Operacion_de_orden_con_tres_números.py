'''Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es
el resto de la división de los dos primeros.'''

#Entradas y/o datos
num1 = int(input('Ingrese el primer numero a continuacion: '))
num2 = int(input('Ingrese el segundo numero a continuacion: '))
num3 = int(input('Ingrese el tercer numero a continuacion: '))

#Procesos

#primero los ordeno de mayor a menor

if num1 > num2 and num1 > num3:
    mayor = num1
    if num2 > num3:
        med=num2
        menor = num3
    else:
        med = num3
        menor = num2
elif num2 > num3:
    mayor = num2
    if num1 > num3:
        med=num1
        menor = num3
    else:
        med=num3
        menor = num1
else:
    mayor=num3
    if num1 > num2:
        med=num1
        menor = num2
    else:
        med=num2
        menor = num1

if menor == (mayor % med):
    print('El numero mas chico es igual al resto de la divison de los otros dos')
else:
    print('El menor no es resto de la division entre los otros dos')