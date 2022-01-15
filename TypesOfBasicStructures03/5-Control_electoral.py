#Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para
# cierto candidato: apellido, nombre y canƟdad de votos. Luego presentar en pantalla un resumen que
# muestre: iniciales del candidato, canƟdad de votos entre paréntesis, y debajo una línea con tantas “x”
# como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea como
# esta: “xxxx” con cuatro letras “x”) (Asumimos que en el centro vecinal no hay demasiados electores,
# de forma que podamos estar seguros que no habrá miles o millones de votos… sólo unos pocos para
# darle senƟdo al enunciado).

'''Entradas'''
apellido = input("Ingrese su apellido a continuación: ")
nombre = input('Ingrese su nombre a continuación: ')
cantidad_votos = int(input('Ingrese la cantidad de votos que representa: '))

'''Procesos'''

'''nos quedamos con las iniciales de su nombre'''
iniciales = apellido[0] + nombre[0]
votos_x = 'x' * cantidad_votos

'''Salida'''
print('Candidato: ( ', iniciales, ' )')
print(votos_x)