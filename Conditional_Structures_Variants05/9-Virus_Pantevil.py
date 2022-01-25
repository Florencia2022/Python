'''Son muchas las concesionarias que en el úlƟmo Ɵempo se han visto afectados por el poderoso
virus PANTEVIL que ataca los registros de automóviles, alterando el identificador de la patente de 
los
mismos. Sabemos que el identi ficador de patente de un automóvil está compuesto por 3 letras en
mayúsculas y 3 números, por ejemplo AED335.
Luego de un exhausƟvo análisis de los registros infectados, se logró decodificar cómo funciona el
virus. Vamos a separar en letras y números para explicar cómo codifica el virus:
Letras:
El virus transforma cada carácter en el entero Unicode al que representa.
Luego chequea si esos tres números son iguales, en caso afirmaƟvo reemplaza los valores del
primer y úlƟmo número por valores aleatorios generados entre 65 y 90.
Una vez que Ɵene esos números, los convierte a cadena de caracteres y los concatena, anteponiendo:
• Un signo @ en caso que los tres números hayan sido iguales o
• Un signo & en caso contrario.
Números:
Para codificar los números el virus uƟliza una cadena con 5 caracteres
El primer carácter codifica:
• Un signo + si los 3 números eran pares y les suma 1 a cada número.
• Un signo - si los 3 números no son pares.
En el segundo carácter el virus pone:
• Un signo # en caso que el primer número y el segundo son iguales, y cambia el valor de
segundo numero por el tercero.
• Un signo $ en caso que el primer número y el tercero son iguales, y cambia el valor de
tercer numero por el segundo.
• Un signo * en caso que el segundo número y el tercero son iguales, y cambia el valor de
tercer numero por el primero.
• Un signo ! en caso que los 3 números sean diferentes.
• En el tercero, cuarto y quinto carácter el virus simplemente concatena los números resultantes.
Finalmente y como si fuera poco, una vez codificados, el virus invierte el orden de los números y
letras. Esto es primero coloca los números codificados y luego las letras codificadas. Veamos algunos
ejemplos:
Patente sin virus   Patente con virus
AED335               -#355&656968
PEP456               -!456&806980
RRR682               +!793@898280
Debido a la gravedad del caso, las concesionarias afectadas no pueden realizar ninguna venta hasta
que no se reparen los archivos dañados, es que nos han solicitado con urgencia un reparador para el
virus PANTEVIL.
'''

