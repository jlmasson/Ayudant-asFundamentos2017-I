intro = input ('Ingrese una palabra: ')

stuart = 0
kevin = 0

vowels = ['a', 'e', 'i', 'o','u']

long = len(intro)

for i in range(0,long):
	for x in range(i+1):
		if intro[x] in vowels:
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
