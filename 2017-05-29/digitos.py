# Dado un número:
# Calcular la cantidad de dígitos que tiene y la respectiva suma de estos

n = int(input("Ingrese valor: ")) # Pido el numero

# Tengo variables de dos tipos:
# Acumuladora -> sumaDigitos
# Contadora -> totalDigitos

# Ambas están inicializas en 0, porque antes de realizar todo el procedimiento
# no se ha sumado ningún digito, y tampoco se ha contado ningún número.
totalDigitos = sumaDigitos = 0

# Yo puedo obtener los dígitos si el cociente es mayor a 0
while n > 0: # n != 0
	
	d = n % 10 # Antes de dividir obtengo el dígito

	sumaDigitos += d # Sumo el dígito

	totalDigitos += 1 # Cuento el dígito. Nótese que es la cantidad de divisiones
	n //= 10 # Actualizo el número

# Muestra por pantalla la suma y el total de dígitos que tiene el número.

print("La suma de los digitos es {}".format(sumaDigitos))
print("El total de dígitos es {}".format(totalDigitos))