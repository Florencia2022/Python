#Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada,
#mostrando la primer letra y la úlƟma, pero reemplazando los caracteres intermedios por asteriscos.
#Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”

'''Entradas'''
palabra = input('Ingrese la palabra a enmascarar: ')

'''Procesos'''

'''Contamos los ateriscos del medio de la palabra, descontandole dos ya que la primera y la ultima letra la vamos a mostrar'''
ateriscos = '*' * (len(palabra) -2)

'''concatenamos los ateriscos con la primera y ultima letra'''
palabra_enmascarada = palabra[0] + ateriscos + palabra[len(palabra)-1]


'''Salidas'''
print('Palabra enmascarada: ', palabra_enmascarada)