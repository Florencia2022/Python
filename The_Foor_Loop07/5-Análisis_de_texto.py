'''El usuario ingresa una frase al comenzar el programa, la misma no puede tener longitud cero. La
frase finaliza con un punto, y las palabras están separadas por espacios unicamente. Se debe mostrar:
Ver el porcentaje de vocales respecto del total de letras de la frase
La longitud promedio de las palabras
La Palabra mas larga del texto
Cantidad de palabras que comienzan con “ta” '''


#Entradas
frase = input('Ingrese la frase(termina con punto):')
cont_palabras = 0   #contamos las palabras para sacar la longitud promedio
cont_vocales = 0    #contamos las vocales 
cont_letras = 0     #contamos las letras para sacar el porcentaje
vocales=('a','e','i','o','u')
cont_ta = 0         #contamos las palabras que empiezen con ta
flag_comienza= True #comienza una palabra nueva
empieza_t = False   #asumimos que no empieza con t
palabra_larga=''
palabra = ''

#Proceso
while len(frase) <= 0:
    print('La frase no  puede tener longitud cero')
    frase = input('Ingrese la frase(termina con punto):')

for i in frase:
    if flag_comienza:
        if i == 't':
            empieza_t = True        #Si empieza con t prendemos la bandera
            flag_comienza = False   #reseteo la bandera
    elif empieza_t:   #si entro en la primera verificacion, entrara en esta en la proxima letra
        if i=='a':
            cont_ta += 1
            empieza_t = False
    if i == ' ' or i== '.':     #Verificamos si la palabra ya termino para contarla
        cont_palabras += 1      #contamos la palabra
        flag_comienza = True    #Prendemos la bandera porque despues de el espacio comienza otra palabra
        if len(palabra) > len(palabra_larga):   #preguntamos si la palbra actual es mayor a la palabra mas larga
            palabra_larga = palabra     #si es asi, palabra pasa a ser la mas larga
        palabra=''          #reseteamos palabra para que guarde la palabra siguiente
    else:
        cont_letras+=1      #contamos las letras
        palabra+=i              #vamos guardando la palabra mientras sea distinto de espacio
    if i in vocales:            #preguntamos si el caracter esta en vocales
        cont_vocales += 1       #si es asi, contamos la vocal.
    

porcentaje_vocal = cont_vocales / cont_palabras
promedio = cont_letras / cont_palabras
print('LA longitud promedio del total de las palabras es de: ', promedio)
print('El porcentaje de las vocales con respecto al total de las letras es de:' ,porcentaje_vocal)
print('La cantidad de palabras que empiezan con ta es igual a: ', cont_ta)
print('La palabra mas larga es: ', palabra_larga)
