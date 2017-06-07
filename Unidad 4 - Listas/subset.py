#
#Autor: Madelyne Velasco
#

"""
Te dan 2 sets: A y B y el trabajo es encontrar si B es un subconjunto de A.
La primera entrada del programa va indicar el número de casos de prueba a realizar.
La primera entrada de cada caso indicará el número de elementos de A
La segunda entrada de cada caso tendrá los elementos de A separados por un espacio
La tercera entrada de cada caso indicará el número de elementos de B
La cuarta entrada de cada caso tendrá los elementos de B separados por un espacio
"""

T = int(input('Numero de casos de prueba a realizar: '))

for x in range(0, T):
	cantidad_a = int(input('Numero de elementos de A: '))
	a = input('Elementos de A: ')

	while cantidad_a != len(a.split()):
		a = input('Elementos de A: ')

	cantidad_b = int(input('Numero de elementos de B: '))
	b = input('Elementos de B: ')

	while cantidad_b != len(b.split()):
		b = input('Elementos de B: ')

	a_elem = a.split()
	b_elem = b.split()

	count = 0
	for z in b_elem:
		if z in a_elem:
			count += 1

	if count == len(b_elem):
		print("True")
	else:
		print("False")