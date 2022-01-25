#Conociendo el precio de lista de un ar􀆡culo, determinar:
#Precio de venta al contado (10 % de descuento)
#Precio de venta con tarjeta (5 % de recargo)

precio_lista=float(input("Ingrese el precio de lista de un articulo: "))

'''Calculamos precio de contado, y precio con tarjeta'''
precio_contado = precio_lista - precio_lista * 10 / 100
precio_tarjeta = precio_lista + precio_lista * 5 / 100

print("El precio de contado de la lista queda en: ", precio_contado)
print("El precio con tarjeta de la lista es de: ", precio_tarjeta)