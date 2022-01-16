'''Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un
jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.'''
 
import random 
#Entradas y/o datos
opcion = 'cara', 'cruz'
opcion_choice = random.choice(opcion)
opcion_elegida = input('Elija a continuacion cara o cruz respectivamente: ')

#Procesos
if opcion_choice == opcion_elegida:
    print('Felicidades, acertaste la apuesta!')
else:  
    print('No se acerto, vuelva a intentar')