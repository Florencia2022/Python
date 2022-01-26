'''Cargar por teclado una frase, pero a razón de un caracter por vez en una variable. La frase debe
terminar con un punto (al aparecer el punto, la carga debe finalizar). El programa debe informar:
Promedio de letras por palabra.
Can dad de palabras que terminan con la letra ’s’ (minúscula).
Can dad de palabras que con enen a la sílaba ’sa’ (minúscula).'''

caracter = ''
cont_letras = 0
cont_palabras = 0
palabras_s = 0
palabras_sa = 0
while caracter != '.':
    caracter=input('Ingrese una frase(de a un caracter a la vez)con punto termina:')
    if caracter !='.' or caracter !=' ':
        cont_palabras += 1
        for i in caracter:
            cont_letras += 1
    if (caracter[len(caracter)-1]) == 's':
        palabras_s += 1
    if (caracter[len(caracter)-2] + caracter[len(caracter)-1]) == 'sa':
        palabras_sa += 1

promedio = cont_palabras / cont_letras

print('El promedio de las letras sobre las palabras es de: ', promedio)
print('La cantidad de palabras que terminaron con s fueron:', palabras_s)
print('La cantidad de palabras que terminaron con sa fueron:', palabras_sa)
