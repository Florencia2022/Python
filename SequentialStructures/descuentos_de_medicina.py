#Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar por teclado }
# el precio de ese medicamento) sabiendo que todos los medicamentos 􀆟enen un descuento del 35 %.
#Mostrar el precio actual, el monto del descuento y el monto final a pagar.

medicamento = "Paracetamol"

'''Ingresamos el precio del medicamento por teclado'''
precio = float(input("Ingrese el precio del: ", medicamento, "a continuacion: "))


descuento = 35

'''Realizamos el calculo del descuento a restar del precio'''
calculo_descuento = descuento * precio // 100

'''restamos el descuento del precio original'''
precio_final = precio - calculo_descuento

print("El precio final del medicamento con un descuento del 35% es de: ", precio_final)