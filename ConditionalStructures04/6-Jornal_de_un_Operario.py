'''Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el
jornal de un determinado operario. Usted deberá cargar por teclado el código de turno
que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas
trabajadas.
La politica de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno
diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo
hace en el turno diurno cobra 35.50 pesos la hora.'''

#Entradas y/o datos

codigo_turno = int(input('Ingrese el codigo de turno: \n 1-Diurno \n 2-Nocturno \n Ingrese el codigo: '))
cantidas_horas = int(input('Ingrese la cantidad de horas trabajadas: '))

#Procesos
#Calculamos el pago dependiendo el turno1
if codigo_turno == 1:
    pago = 35.50 * cantidas_horas
else:
    pago = 40.60 * cantidas_horas

#Salidas
print('El pago por la cantidad de horas trabajadas es de: ', pago)