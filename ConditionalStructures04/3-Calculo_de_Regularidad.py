#La facultad pide un simple programa que pida las tres notas de un alumno en cualquier materia
#y mostrar si el alumno esta libre, regular o promocionado. Las tres notas son los dos parciales mas la
#nota de prácƟcos y las condiciones de regularidad están descriptas a conƟnuación:
#El promedio menor a 4 el alumno esta libre
#El promedio comprendido entre 4 y 8 el alumno esta regular
#El promedio mayor a 8 el alumno está promocionado.

'''Entradas y/o datos'''
primer_nota = float(input('Ingrese la nota del primer parcial: '))
segunda_nota = float(input('Ingrese la nota del segundo parcial: '))
nota_practicos = float(input('Ingrese la nota de practicos: '))

'''Procesos'''
'''sacamos el promedio antes que nada'''
promedio = (primer_nota + segunda_nota + nota_practicos) / 3

'''Verificamos el promedio para resolver la condicion'''

if promedio < 4:
    condicion = 'Libre'
elif promedio < 8:
    condicion = 'Regular'
else:
    condicion = 'Promocionado'

'''Salidas'''
print('La condicion del alumno es:', condicion)