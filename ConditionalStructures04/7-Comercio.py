'''Un comerciante tiene a la venta 3 tipos de articulos principales. Conociendo la cantidad vendida
de cada articulo y el precio unitario de cada articulo, hacer un programa que determine cuál fue el
producto que realizó el mayor aporte en los ingresos y el porcentaje que dicho aporte significa en el
ingreso absoluto de los 3 articulos sumados. Ese porcentaje se calcula así: Absoluto = 100 %
Mayor aporte = x %'''

#DATOS Y/O ENTRADAS
art1 = input('Ingrese el nombre del articulo 1: ')
cantidad1 = int(input('Ingrese la cantidad del articulo 1: '))
precio_unitario1 = float(input('Ingrese el precio unitario del articulo 1: '))

art2 = input('Ingrese el nombre del articulo 2: ')
cantidad2 = int(input('Ingrese la cantidad del articulo 2: '))
precio_unitario2 = float(input('Ingrese el precio unitario del articulo 2: '))

art3 = input('Ingrese el nombre del articulo 3: ')
cantidad3 = int(input('Ingrese la cantidad del articulo 3: '))
precio_unitario3 = float(input('Ingrese el precio unitario del articulo 3: '))

#Procesos
#Calculamos primero las ganancias de cada articulo
gananacia1 = cantidad1 * precio_unitario1
ganancia2 = cantidad2 * precio_unitario2
ganancia3 = cantidad3 * precio_unitario3

#Guardamos en una variable el articulo con mayor ganancia
if gananacia1 > ganancia2 and gananacia1 > ganancia3:
    mayor = art1, gananacia1
elif ganancia2 > ganancia3:
    mayor = art2, ganancia2
else:
    mayor = art3, ganancia3

total = gananacia1 + ganancia2 + ganancia3
porcentaje = mayor[1] * 100 / total

#Salidas
print("El articulo que mayor ganancia tuvo: ", mayor[0])
print("El un porcentaje: ", porcentaje)

