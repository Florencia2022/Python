#Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de la
#base, pero sabiendo que su altura es igual al cuadrado de la base. (Observar que la altura no es un
#dato… sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).

base = float(input("Ingrese el valor de la base a evaluar: "))
altura = base ** 2

area = (base * altura) / 2

print("El area de un triangulo es de: ", area )