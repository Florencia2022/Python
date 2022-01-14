#Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores a y b, que:
#Un binomio al cuadrado (suma) esigual al cuadrado del primer término, más el doble producto del
# #primero por el segundo más el cuadrado del segundo.

a = int(input("Ingrese el primer valor: "))
b = int(input("ingrese el segundo valor: "))

binomio = (a ** 2) + (2*a*b) + (b ** 2)

print("El cuadrado al binomio de los dos enteros es de: ", binomio)