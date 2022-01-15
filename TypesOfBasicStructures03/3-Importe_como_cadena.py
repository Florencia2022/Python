#Desarrollar un programa que cargue por teclado un importe (canƟdad de dinero) expresado como
#número en coma flotante y muestre un mensaje con esa canƟdad pero en dos formatos: en uno debe
#aparecer precedida por el signo “$” y en el otro debe aparecer precedida por la palabra “pesos”.

'''Entradas'''
importe = float(input("Ingrese el importe a procesar: "))

'''Procesos'''

'''Lo pasamos a string para poder concatenarlo con los siguientes formatos'''
importe_str = str(importe)

'''Le agregamos el signo pesos, del primer formato'''
formato1 = '$ ' + importe_str

'''Lo agregamos la palabra 'pesos' del segundo formato'''
formato2 = importe_str + ' pesos'

'''Salidas'''
print('Primer formato: ', formato1)
print('Segundo formato: ', formato2)