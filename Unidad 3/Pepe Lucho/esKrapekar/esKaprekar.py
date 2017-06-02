#
#Autor: José Luis Masson (Pepe Lucho)
#


n = int(input("Ingrese número: ")) # Pido el número

cuadrado = n ** 2 # Elevo el numero al cuadrado

suma = 0 # Inicio la variable suma en 0

i = 1	# Inicio la variable i (exponente) en 1

aux = cuadrado # Creo una variable auxiliar para dividir de manera sucesiva.

# Esta es la condición de continuación del lazo
# obtenidos a partir de la compresión de los 3 ejemplos mostrados
while (aux > 0 and suma != n):

	# Cada vez que se divide, el divisor se multiplica por 10
	divisor = 10 ** i

	# Obtengo el cociente y residuo
	c = cuadrado // divisor
	r = cuadrado % divisor

	suma = c + r
	i += 1

	# Actualizo el auxiliar
	# En el 3er ejemplo se aprecia que el lazo se detiene
	# porque el cociente da como resultado 0
	aux //= 10

# Pregunto si la suma al final es igual al numero n ingresado
if (suma == n):
	print("El numero es Kaprekar")
else:
	print("El numero no es Kaprekar")
