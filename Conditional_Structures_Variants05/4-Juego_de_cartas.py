'''Desarrollar un programa para implementar un juego de cartas de la baraja española.
Es una competencia de 3 rondas entre 2 jugadores.
En cada ronda, cada jugador recibe una carta (cuyo número y palo el programa deberá generar de
forma aleatoria) y se define la ronda de la siguiente manera:
El jugador que tenga la carta de mayor valor, se lleva ambas.
Si las cartas son del mismo valor, se las lleva quien tenga una carta de oro.
Si ninguno tiene oro, cada jugador recupera su carta.
Los puntos de cada jugador se determinan sumando los valores de todas las cartas que ganó. Será
triunfador el que tenga mayor puntaje total.
'''
#datos y/o entradas

#guardamos los puntos en dos contadores, uno para cada jugador
cont1 = 0
cont2 = 0

import random

palos = 'oro', 'espada', 'basto', 'copa'

print('Ronda - 1')

ronda1_num1 = random.randint(1,12)
ronda1_palo1 = random.choice(palos)
print('Jugador 1 obtiene: ', ronda1_num1, 'de: ', ronda1_palo1)

ronda1_num2 = random.randint(1,12)
ronda1_palo2 = random.choice(palos)
print('Jugador 2 obtiene: ', ronda1_num2, 'de: ', ronda1_palo2)

if ronda1_num1 > ronda1_num2:
    cont1 += 1
    print('Gana jugador 1, tiene la carta mas alta.')
elif ronda1_num1 == ronda1_num2:
    if ronda1_palo1 == 'oro':
        cont1 += 1
        print('Gana jugador 1, en el empate de numeros gana el que tiene oro')
    elif ronda1_palo2 == 'oro':
        cont2 +=1
        print('Gana jugador 2, en el empate de numeros gana el que tiene oro')
    else:
        print('Empate')
else:
    cont2 += 1
    print('Gana jugador 2, tiene la carta mas alta. ')


print('Ronda - 2')

ronda2_num1 = random.randint(1,12)
ronda2_palo1 = random.choice(palos)
print('Jugador 1 obtiene: ', ronda2_num1, 'de: ', ronda2_palo1)

ronda2_num2 = random.randint(1,12)
ronda2_palo2 = random.choice(palos)
print('Jugador 2 obtiene: ', ronda2_num2, 'de: ', ronda2_palo2)

if ronda2_num1 > ronda2_num2:
    cont1 += 1
    print('Gana jugador 1, tiene la carta mas alta.')
elif ronda2_num1 == ronda2_num2:
    if ronda2_palo1 == 'oro':
        cont1 += 1
        print('Gana jugador 1, en el empate de numeros gana el que tiene oro')
    elif ronda2_palo2 == 'oro':
        cont2 +=1
        print('Gana jugador 2, en el empate de numeros gana el que tiene oro')
    else:
        print('Empate')
else:
    cont2 += 1
    print('Gana jugador 2, tiene la carta mas alta. ')



print('Ronda - 3')

ronda3_num1 = random.randint(1,12)
ronda3_palo1 = random.choice(palos)
print('Jugador 1 obtiene: ', ronda3_num1, 'de: ', ronda3_palo1)

ronda3_num2 = random.randint(1,12)
ronda3_palo2 = random.choice(palos)
print('Jugador 2 obtiene: ', ronda3_num2, 'de: ', ronda3_palo2)

if ronda3_num1 > ronda3_num2:
    cont1 += 1
    print('Gana jugador 1, tiene la carta mas alta.')
elif ronda3_num1 == ronda3_num2:
    if ronda3_palo1 == 'oro':
        cont1 += 1
        print('Gana jugador 1, en el empate de numeros gana el que tiene oro')
    elif ronda3_palo2 == 'oro':
        cont2 +=1
        print('Gana jugador 2, en el empate de numeros gana el que tiene oro')
    else:
        print('Empate')
else:
    cont2 += 1
    print('Gana jugador 2, tiene la carta mas alta. ')


# Salida

if cont1 > cont2:
    print('Felicidades jugador 1, gano')
else:
    print('Felicidades jugador 2, gano')