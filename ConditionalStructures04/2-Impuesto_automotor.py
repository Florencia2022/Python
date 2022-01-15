# Crear un programa que permita calcular los impuestos que debe pagar un auto, conociendo su
#modelo (año de fabricación) y Ɵpo (P: ParƟcular/T: Taxi/R: Remis). Para calcular los impuestos, tener
#en cuenta que:
#Los autos parƟculares de menos de 10 años de anƟgüedad pagan $200, entre 10 y 20 años pagan
#$150 y no pagan impuestos los que Ɵenen más de 20 años.
#Los taxis pagan impuestos como auto parƟcular, más $150 por la licencia de taxi.
#Los remises pagan $100 por cada año de anƟgüedad de su vehículo

'''Entradas'''

modelo = int(input('Ingrese el modelo del auto, en formato aaaa: '))
tipo =  int(input('Ingrese la opcion que corresponda a su tipo de auto: \n 1-Particular \n 2-Taxi \n 3-Remis \n Ingrese un numero a continuacion: '))

'''Si es particular o taxi agregamos el impuesto dependiendo de la antiguedad'''
if tipo == 1 or tipo == 2:
    if modelo < 10:
        impuestos = 200
    elif modelo < 20:
        impuestos = 150
    else:
        impuestos = 0
    '''Si es un taxi le agregamos a impuestos los $150 de la patente'''
    if tipo == 2:
        impuestos = impuestos + 150

else: #Si no es ni particular ni taxi, por deduccion es remis y multiplicamos su antiguedad por 100
    impuestos = modelo * 100

'''Salidas'''
print('El impuesto a pagar por su auto es de: $', impuestos)