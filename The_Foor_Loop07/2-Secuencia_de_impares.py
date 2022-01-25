'''Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos
entre ellos, en forma ascendente y descendente'''

#Entradas
num1=int(input('Ingrese el primer numero: '))
num2=int(input('Ingrese el segundo numero: '))

#busco cual es el mayor para saber en donde termina la secuencia de impares.
if num1 > num2:
    mayor=num1
    menor=num2
else:
    mayor=num2
    menor=num1

print('IMPARES ASCENDENTE')
if menor%2 ==0:
    menor+=1
for i in range(menor,mayor+1, 2):
    print(i)

print('IMPARES DESCENDENTES')
if mayor%2 == 0:
    mayor-=1

for i in range(mayor,menor-1,-2):
    print(i)