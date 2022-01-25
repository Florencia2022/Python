'''Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y
luego:
Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
Determinar en qué mes recibió el sueldo más bajo del período.
Informar el sueldo promedio del semestre.'''
import random
#Entradas
suma_sueldo = 0
sueldo_alto = -1
sueldo_bajo = -1
cont_mes = 0
promedio = 0


#Proceso
for i in range(1, 7):
    sueldo = random.randint(10,80)
    print(sueldo)
    suma_sueldo += sueldo
    if sueldo > sueldo_alto or sueldo_alto == -1:
        sueldo_alto = sueldo 
    elif sueldo < sueldo_bajo or sueldo_bajo== -1:
        sueldo_bajo = sueldo
        cont_mes = i

promedio = suma_sueldo/6

meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio')


#Salidas
print('El sueldo mas bajo es:', sueldo_bajo, 'en el mes:' , meses[cont_mes-1]) 
print('El sueldo mas alto es:' , sueldo_alto)
print('Promedio: ', promedio)
