#Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado
# es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado
# al cubo.

'''Entradas'''

a = float(input('Ingrese el primer número a evaluar: '))
b = float(input('Ingrese el segundo número a evaluar: '))
c = float(input('Ingrese el tercer número a evaluar: '))

'''Proceso'''
resultado  = a + b + c

'''Preguntamos si el resultado es mayor a 10'''
if resultado > 10: 
    resultado_final = resultado // 2
else:
    resultado_final = resultado ** 3

'''Salidas'''
print('La suma de los 3 números es:', resultado)
print('Por lo tanto el resultado final es de: ', int(resultado_final))