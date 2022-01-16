'''Según la Ley Electoral de la República ArgenƟna, el Presidente y el Vicepresidente se eligen de
acuerdo a las siguientes reglas:
ArTIculo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %)
de los votos afirmativos válidamente emitidos; en su defecto, aquella que hubiere obtenido el cuarenta
por ciento (40 %) por lo menos de los votos afirmaƟvos válidamente emiƟdos y, además, exisƟere una
diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmaƟvos válidamente
emiƟdos, sobre la fórmula que le sigue en número de votos.
Arơculo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escruƟnio
ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la
Asamblea LegislaƟva atento lo dispuesto por el arơculo 120 de la presente ley, se realizará una segunda
vuelta dentro de los treinta (30) días.
Arơculo 151. — En la segunda vuelta parƟciparán solamente las dos fórmulas más votadas en la
primera, resultando electa la que obtenga mayor número de votos afirmaƟvos válidamente emiƟdos.
Desarrollar un programa que permita ingresar, para los 3 partidos más votados: fórmula (presidente + vice) y 
cantidad de votos obtenidos.
Luego determinar:
Qué fórmula obtuvo el mayor porcentaje.
Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes
parƟcipan de la segunda vuelta'''

#Entrada y/o datos

formula1 = input('Formula N°1-Ingrese a su presidente y vice presidente a continuacion: ')
cantidad1 = int(input('Ingrese la cantidad de votos que obtuvieron a continuacion: '))


formula2 = input('Formula N°2-Ingrese a su presidente y vice presidente a continuacion: ')
cantidad2 = int(input('Ingrese la cantidad de votos que obtuvieron a continuacion: '))


formula3 = input('Formula N°3-Ingrese a su presidente y vice presidente a continuacion: ')
cantidad3 = int(input('Ingrese la cantidad de votos que obtuvieron a continuacion: '))

#Procesos
#Para poder saber lo demas sacamos el porcentaje de cada una
total_votos = cantidad1 + cantidad2 + cantidad3
porcentaje1 = cantidad1 * 100 / total_votos
porcentaje2 = cantidad2 * 100 / total_votos
porcentaje3 = cantidad3 * 100 / total_votos

#Articulo 151
if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
    primero = porcentaje1
    f1 = formula1
    if porcentaje2 > porcentaje3:
        segundo = porcentaje2
        f2 = formula2
    else:
        tercero = porcentaje3
        f3 = formula3
elif porcentaje2 > porcentaje3:
    primero = porcentaje2
    f1 = formula2
    if porcentaje1 > porcentaje3:
        segundo = porcentaje1
        f2 = formula1
        tercero = porcentaje3
        f3 = formula3
    else:
        segundo = porcentaje3
        f2 = formula3
        tercero = porcentaje1
        f3 = formula1
else: 
    primero = porcentaje3
    f1 = formula3
    if porcentaje1 > porcentaje2:
        segundo = porcentaje1
        f2 = formula1
        tercero = porcentaje2
        f3 = formula3
    else:
        segundo = porcentaje2
        f2 = formula2
        tercero = porcentaje1
        f3 = formula2

if primero >=45 or primero >40 and (primero - segundo) > 10:
    print('La formula resulto elegida, no hay segunda vuelta.')
else:
    print('Hay segunda vuelta. los participantes son: ')
    print(f1)
    print(f2)

#Salidass

print('La formula que obtuvo el mayor porcentaje fue: ', f1)