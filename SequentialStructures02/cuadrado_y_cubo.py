#Leer dos números y calcular:La suma de sus cuadrados.El promedio de sus cubos.

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))

cuadradoA = a**2
cuadradoB = b**2
suma_de_cuadrados = cuadradoA + cuadradoB

cuboA = a**3
cuboB = b**3
promedio_de_cubos = ( cuboA + cuboB ) / 2

print("La suma de los cuadrados del primer numero con el segundo es de: ", suma_de_cuadrados)
print("El promedio de los cubos de los dos numeros ingresados es de: ", promedio_de_cubos)