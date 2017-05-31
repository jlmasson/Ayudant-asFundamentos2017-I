n = int(input("Ingrese valor: "))

totalDigitos = sumaDigitos = 0

while n > 0: # n != 0
	d = n % 10
	sumaDigitos += d
	totalDigitos += 1
	n //= 10

print("La suma de los digitos es {}".format(sumaDigitos))
print("El total de dígitos es {}".format(totalDigitos))