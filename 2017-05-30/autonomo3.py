# Para menús, se trata de emular lo que hace un lazo do - while (no disponible en Python)
# El lazo do - while, primero ejecuta las sentencias del lazo, y luego verifica la condición.
# En cambio, el lazo while primero verifica y después ejecuta las sentencias del lazo.
# Con el lazo do - while se asegura que al menos el código se ejecute una vez.

# Para emular esto, se crea una variable con valor booleano False (de acuerdo al problema)
# para mí False indica que no ha salido.
# Y me aseguro que el código se ejecuta al menos una vez
salir = False

# Nota: Solo utilizar banderas booleanas para la parte de los menús de un programa.
# Las demás partes del programa, evitar usar banderas booleanas.
# Basarse siempre en condiciones de salida y continuación del lazo.

# Inicializo con cadenas vacías, puesto que se van actualizar dentro del lazo while
vehiculos = ""
ventas1S = ""
ventas2S = ""

while not(salir): # salir == False
	# Este es el menú que se mostrará por pantalla
	print("1. Ingreso de Vehículos")
	print("2. Ingreso de Ventas por semestre")
	print("3. Presentar ventas por rango")
	print("4. Presentar vehículo con mayor venta por semestre")
	print("5. Salir")

	op = int(input("Ingrese opción [1-5]: "))

	if op == 1:
		# Valido si la cadena esta vacia, con esto me aseguro de no alterar
		# los valores después
		if len(vehiculos) == 0:
			vehiculos = input("Ingrese vehiculos separados por comas: ")
			vehiculos = vehiculos.split(",")
		else:
			print("Ya ha ingresado vehículos al sistema.")
	elif op == 2:
		print("1. Semestre enero-junio.")
		print("2. Semestre julio-diciembre.")
		opSub = int(input("Ingresa semestre: "))
		if opSub == 1:
			# Debo validar si la lista de vehiculos está con datos.
			# No tiene sentido llenar la lista de ventas con la lista de vehículos vacía.
			if len(vehiculos) != 0:
				ventas1S = input("Ingrese ventas primer semestre: ")
				ventas1S = ventas1S.split(",")
				# Aquí valido la parte que debe cumplir la misma cantidad de elementos
				# separados por comas, con respecto a la cantidad de vehículos
				while len(ventas1S) != len(vehiculos):
					print("Ingrese la cantidad correcta de valores.")
					ventas1S = input("Ingrese ventas primer semestre: ")
					ventas1S = ventas1S.split(",")
				# Procedo a convertir a enteros cada uno de los valores.
				for i, venta in enumerate(ventas1S):
					ventas1S[i] = int(venta)
			else:
				print("Debes ingresar por lo menos 1 vehículo.")
		elif opSub == 2:
			# Misma funcionalidad que la opción 1
			if len(vehiculos) != 0:
				ventas2S = input("Ingrese ventas segundo semestre: ")
				ventas2S = ventas2S.split(",")
				while len(ventas2S) != len(vehiculos):
					print("Ingrese la cantidad correcta de valores.")
					ventas2S = input("Ingrese ventas segundo semestre: ")
					ventas2S = ventas2S.split(",")
				for i, venta in enumerate(ventas2S):
					ventas2S[i] = int(venta)
			else:
				print("Debes ingresar por lo menos 1 vehículo.")
		else:
			# En caso de que ingrese cualquier numero, se le muestra esto al usuario
			print("Vuelve a ingresar una opción válida.")
	elif op == 3:
		# Para poder mostrar un rango, debo saber que la lista debe contener
		# al menos un valor
		if len(vehiculos) != 0:
			inicio = int(input("Ingrese inicio: "))
			fin = int(input("Ingrese fin: "))

			# Debo validar que el inicio siempre sea menor que el fin
			while inicio > fin or inicio < 0 or fin < 0:
				print("Ingrese valores válidos.")
				inicio = int(input("Ingrese inicio: "))
				fin = int(input("Ingrese fin: "))

			# Una vez validado, muestro por pantalla los elementos que cumplen con
			# este rango.
			for i, v in enumerate(vehiculos):
				totalV = ventas1S[i] + ventas2S[i]
				if totalV >= inicio and totalV <= fin:
					print("Producto: {} {}".format(v, totalV))
		else:
			print("Debes ingresar por lo menos 1 vehículo")
	elif op == 4:
		# Vehículo con venta máxima de 1er semestre
		ventaMax1S = max(ventas1S)
		vehiculo1S = vehiculos[ventas1S.index(ventaMax1S)]
		# Vehículo con venta máxima de 2do semestre
		ventaMax2S = max(ventas2S)
		vehiculo2S = vehiculos[ventas2S.index(ventaMax2S)]

		print("Producto con mayor venta en semestre 1: {} {}".format(vehiculo1S, ventaMax1S))
		print("Producto con mayor venta en semestre 2: {} {}".format(vehiculo2S, ventaMax2S))	
	elif op == 5:
		salir = True
	else:
		print("Ingrese opción válida.")