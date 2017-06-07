#
#Autor: Madelyne Velasco
#

"""
A ambos jugadores se les da una string de tamaño S y ambos tienen que hacer substrings usando las letras de S (Estas substrings son consecutivas)
Stuart tiene que hacer substrings que empiecen con consonantes mientras que Kevin tiene que hacer substrings que empiecen con vocales
Cada jugador gana un punto por cada substring. Tu trabajo es determinar quien gana el juego.
"""

intro = input ('Ingrese una palabra: ')

stuart = 0
kevin = 0

vowels = ['a', 'e', 'i', 'o','u']

long = len(intro)

for i in range(0,long):
	for x in range(i+1):
		if intro[i] in vowels:
			slc = intro[i:x]
			kevin = kevin + 1
		else:
			slc = intro[i:x]
			stuart = stuart +1

if stuart > kevin:
	print('Stuart ',stuart)
elif kevin > stuart:
	print('Kevin ' ,kevin)
else:
	print('Draw')
