#Se tienen los datos de tres postulantes a un empleo, a los que se les realizó un test de capacitación.
#Por cada postulante, se tiene entonces la siguiente información: nombre del postulante, canƟdad total
#de preguntas que se le realizaron y cantidad de preguntas que contestó correctamente.
#Se pide confeccionar un programa que lea los datos de los tres postulantes, informe el nivel de cada
#uno según los criterios de aprobación que se indican mas abajo, e indique finalmente el nombre del
#postulante que ganó el puesto. Los criterios de aprobación son los siguientes, en función del porcentaje
#de respuestas correctas sobre el total de preguntas realizadas a cada postulante:
#Nivel Superior: Porcentaje 90 %
#Nivel Medio: 75 <= Porcentaje < 90 %
#Nivel Regular: 50 <= Porcentaje < 75 %
#Fuera de Nivel: Porcentaje < 50 %

'''Entradas y/o datos'''
#datos de postulante 1
p1_nombre = input('Ingrese el nombre de postulante 1: ')
p1_preguntas_totales = int(input('Ingrese la cantidad de preguntas realizadas: '))
p1_preguntas_correctas = int(input('Ingrese la cantidad de preguntas correctas: '))

#Datos de postulante 2
p2_nombre = input('Ingrese el nombre de postulante 2: ')
p2_preguntas_totales = int(input('Ingrese la cantidad de preguntas realizadas: '))
p2_preguntas_correctas = int(input('Ingrese la cantidad de preguntas correctas: '))

#Datos de postulante 3
p3_nombre = input('Ingrese el nombre de postulante 3: ')
p3_preguntas_totales = int(input('Ingrese la cantidad de preguntas realizadas: '))
p3_preguntas_correctas = int(input('Ingrese la cantidad de preguntas correctas: '))

'''Procesos'''

'''Sacamos el porcentaje de preguntas correctas de cada postulante'''
porcentaje1 = p1_preguntas_correctas / p2_preguntas_totales * 100
porcentaje2 = p2_preguntas_correctas / p2_preguntas_totales * 100
porcentaje3 = p3_preguntas_correctas / p3_preguntas_totales * 100

'''Calculamos el nivel del postulante 1'''
if porcentaje1 > 90:
    nivel1 = 'Nivel Superior'
elif porcentaje1 >= 75:
    nivel1 = 'Nivel Medio'
elif porcentaje1 >= 50:
    nivel1 = 'Nivel Regular'
else:
    nivel1 = 'Fuera de Nivel'

'''Calculamos el nivel del postulante 2'''
if porcentaje2 > 90:
    nivel2 = 'Nivel Superior'
elif porcentaje2 >= 75:
    nivel2 = 'Nivel Medio'
elif porcentaje2 >= 50:
    nivel2 = 'Nivel Regular'
else:
    nivel2 = 'Fuera de Nivel'

'''Calculamos el nivel del postulante 3'''
if porcentaje3 > 90:
    nivel3 = 'Nivel Superior'
elif porcentaje3 >= 75:
    nivel3 = 'Nivel Medio'
elif porcentaje3 >= 50:
    nivel3 = 'Nivel Regular'
else:
    nivel3 = 'Fuera de Nivel'


if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
    nombre_mejor = p1_nombre
    porcentaje_mejor = porcentaje1
    nivel_mejor = nivel1
elif porcentaje2 > porcentaje3:
    nombre_mejor = p2_nombre
    porcentaje_mejor = porcentaje2
    nivel_mejor = nivel2
else:
    nombre_mejor = p3_nombre
    porcentaje_mejor = porcentaje3
    nivel_mejor = nivel3

'''Salidas'''
#Mostramos los niveles de los postulantes:
print('El nivel del postulante numero 1 es de: ', nivel1)
print('El nivel del postulante numero 2 es de: ', nivel2)
print('El nivel del postulante numero 3 es de: ', nivel3)

print('El nombre del postulante que tuvo mas respuestas correctas fue:', nombre_mejor)