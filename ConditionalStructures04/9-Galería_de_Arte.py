'''Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba
con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá verificar si
todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y
terminó en el año 2000). Determinar cuántos tenen antgüedad inferior a 10 años. Si no hay ninguno,
imprimir el mensaje “Renovar stock”.'''

#Datos y/o entradas
cuadro1 = int(input('Ingrese el año en el que fue creado el cuadro 1: '))
cuadro2 = int(input('Ingrese el año en el que fue creado el cuadro 2: '))
cuadro3 = int(input('Ingrese el año en el que fue creado el cuadro 3: '))

#determinamos la antiguedad
anio_actual = 2022
antiguedad1 = anio_actual - cuadro1
antiguedad2 = anio_actual - cuadro2
antiguedad3 = anio_actual - cuadro3

#Determinar si todos los cuadros son anteriores al siglo 20,(menores al año 1901)
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901:
    print('Las obras son todas antiguas')

#Determinar cuántos tenen antgüedad inferior a 10 años.
cont_antiguedad = 0
if antiguedad1 < 10:
    cont_antiguedad += 1
if antiguedad2 < 10:
    cont_antiguedad += 1
if antiguedad3 < 10:
    cont_antiguedad += 1

if cont_antiguedad ==0 :
    print('Renovar stock')
else:
    print('Hay obras disponibles.')