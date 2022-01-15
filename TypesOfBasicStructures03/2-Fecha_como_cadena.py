#Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato “dd/mm/aaaa”, y muestre por separado el día, el mes y el año. Ejemplo:
#si la cadena ingresada es “16/03/2015” el programa debe mostrar: “Día: 16 - Mes: 03 - Año: 2016”

'''Entradas'''
fecha = input("Ingrese la fecha en formato dd/mm/aaaa, incluyendo  ceros: ")

'''Procesos'''

'''Agregamos a una nueva variable dia que pertenecen a los dos primeros caracteres'''
dia = fecha[0] + fecha[1]

'''El mes pertenecen a los caracteres 3 y 4'''
mes = fecha[3] + fecha[4]

'''El año pertenecen a los ultimos cuatro caracteres'''
anio = fecha[6] + fecha[7] + fecha[8] + fecha[9]

'''Salidas'''
print('Dia: ', dia, 'Mes: ', mes, 'Año: ', anio)