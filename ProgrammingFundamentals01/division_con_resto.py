#Plantear un script (directamente en el shell de Python) que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división.

a = int(input("Ingrese el primer valor(de tipo entero): "))
b = int(input("Ingrese el segundo valor(de tipo entero): "))

print("La division del primer numero: ", a, "dividido el segundo: ", b, "es igual a: ", a/b, "con resto: ", a%b)