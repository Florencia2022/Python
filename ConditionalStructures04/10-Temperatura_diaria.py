'''Se solicita realizar un programa que permita generar tres temperaturas en forma aleatoria (correspondientes a diferentes momentos de un día) y determinar:
Cual es el promedio de las temperaturas
Si existe alguna temperatura que sea mayor al promedio'''

#Entrada y/o datos
temp1 = round(15, 45)
temp2 = round(15, 45)
temp3 = round(15,45)

#Procesos

#calculamos el promedio
promedio = (temp1 + temp2 + temp3) / 3

if temp1 > promedio or temp2 > promedio or temp3 > promedio:
    print('Existen temperaturas mayor al promedio.')
else:
    print('No existen temperaturas mayor al promedio.')

print('Temperatura 1: ', temp1)
print('Temperatura 2: ', temp2)
print('Temperatura 3: ', temp3)
