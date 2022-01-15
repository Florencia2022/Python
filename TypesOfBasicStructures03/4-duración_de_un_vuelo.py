#Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos), 
# determine cuál es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir 
# del aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?

'''Entradas y datos'''
tiempo_taxi_hotel= 45

partida = input('Ingrese el horario de partida en formato hh:mm, a continuacion: ')
llegada = input('Ingrese el horario de llegada en formato hh:mm a continuación: ')

'''Procesos'''

'''Separamos las horas de los minutos del horario de partida'''
horas_partida = partida[0] + partida[1]
min_partida = partida[3] + partida[4]

'''calculamos el horario de partida en minutos'''
partida_en_minutos = min_partida + horas_partida * 60

'''Separamos las horas de los minutos del horario de llegada'''
horas_llegada = llegada[0] + llegada[1]
min_llegada = llegada[3] + llegada[4]

'''calculamos el horario de llegada en minutos'''
llegada_en_minutos = min_llegada + horas_llegada * 60

'''Calculamos la duracion del viaje'''
duracion_viaje_minutos = (int(llegada_en_minutos) - int(partida_en_minutos)) + tiempo_taxi_hotel
'''Resultados'''
print('La duracion del viaje en minutos fue de:', duracion_viaje_minutos)