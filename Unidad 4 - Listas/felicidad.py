#
#Autor: Madelyne Velasco
#

"""
Tienes un arreglo de n elementos y 2 conjuntos separados A y B que contienen m enteros.
Todos los elementos en A te gustan y todos los de B te desagradan.
Tu felicidad incial es de 0.
Por cada elemento que pertenece a A, tu felicidad aumenta en uno y por cada elemento que pertenece a B, disminuye en 1.
El conjunto inicial no tiene elementos repetidos pero A y B si los pueden tener.
"""

n = int(input('Ingrese la cantidad de elementos totales: '))
m = int(input('Ingrese el tamaño de los conjuntos A y B: '))

total = []
a = []
b = []
felicidad = 0

for i in range(0, n):
	x = int(input('Ingresa un elemento: '))
	if x not in total:
		total.append(x)
	else:
		while(x in total):
			x = int(input('Ingresa un elemento que no este en la lista: '))
		total.append(x)

print('Ahora ingresa los elementos del conjunto A: ')
for i in range(0, m):
	x = int(input('Ingresa un elemento para A: '))
	a.append(x)

print('Ahora ingresa los elementos del conjunto B: ')	
for i in range(0, m):
	x = int(input('Ingresa un elemento para B: '))
	b.append(x)

#Verificacion

for x in a:
	if x in total:
		felicidad += 1

for x in b:
	if x in total:
		felicidad -= 1

print(felicidad)