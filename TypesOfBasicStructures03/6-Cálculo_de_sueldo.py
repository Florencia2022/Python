#Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional
#al cual pertenece. Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento
#del 8 % sobre su salario actual y un descuento de 2,5 % por servicios, informando los resultados.

'''Entradas'''
nombre = input('Ingrese el nombre del empleado: ')
salario_actual = float(input('Ingrese el salario actual del empleado: '))
area = input('Ingrese el area del empleado al cual pertenece: ')

'''Procesos'''
aumento = salario_actual * 0.08
descuento  = salario_actual * 0.025

salario_new = salario_actual + aumento - descuento

'''Salidas'''
print('Nombre Empleado: ', nombre, '\t\t Nuevo Salario: $', salario_new)
print('Área Funcional: ', area)
print('Salario Actual: $', salario_actual)