'''Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra,
papel o tijera” y determine cuál de ellos es el ganador. Las reglas son:
La piedra aplasta (o rompe) la tijera. (Gana la piedra).
La tjera corta el papel. (Gana la tijera).
El papel envuelve la piedra. (Gana el papel)
Si los dos jugadores eligen el mismo elemento, empatan.
'''

#Entradas y/o datos
import random


maquina = random.randint('1, 2, 3')
humano = int(input('Ingrese la opcion a elegir: \n 1-Piedra \n 2-Papel \n 3-Tijera \Ingrese su opcion a continuación: '))

if maquina == humano:
    print('Empate')
elif maquina == 1 and humano == 3 or maquina == 3 and humano == 2 or maquina == 2 and humano == 1:
    print('Lo sentimos, perdiste')
else:
    print('Ganaste la partida!')