n = int(input("Ingrese número: "))

aux = n

cuadrado = n ** 2

suma = 0

i = 1

while (aux > 0 and suma != n):

	divisor = 10 ** i
	c = cuadrado // divisor
	r = cuadrado % divisor

	suma = c + r
	i += 1
	aux //= 10

if (aux == 0 and suma == n):
	print("El numero es Kaprekar")
else:
	print("El numero no es Kaprekar")
