#En el Congreso se vota la sanción de una ley muy importante. Desarrollar un programa que permita
#ingresar la canƟdad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso.

'''Entradas'''

votos_favor = int(input("Ingrese los votos a favor: "))
votos_contra = int(input("Ingrese los votos en contra: "))

'''Procesos'''

total_votos = votos_favor + votos_contra

'''Calculamos el porcentaje de votos a favor'''
porcentaje_a_favor = votos_favor / total_votos * 100

'''Calculamos el porcentaje de votos en contra'''
porcentaje_en_contra = votos_contra / total_votos * 100


'''Salidas'''
print("El total de los voto es de:", total_votos)
print("Porcentaje de votos a favor: ", porcentaje_a_favor, "%")
print("Porcentaje de votos en contra: ", porcentaje_en_contra, "%")