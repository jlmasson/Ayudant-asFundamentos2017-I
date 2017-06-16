#
#Autor: Madelyne Velasco
#

"""
Se te da una string S y debes hacer que cada incial de palabra dentro de S sea mayúsculas.

"""

intro = input('Ingresa tu frase: ')
res = intro.split()
result = ''
for word in res:
	long = len(word)
	for i in range(0, long):
		if i == 0:
			result = result+word[i].upper()
		else:
			result = result+word[i]  
	result = result+' '
print (result)