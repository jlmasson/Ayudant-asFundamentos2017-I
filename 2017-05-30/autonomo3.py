

salir = False
vehiculos = ""
ventas1S = ""
ventas2S = ""

while not(salir): # salir == False
	print("1. Ingreso de Vehículos")
	print("2. Ingreso de Ventas por semestre")
	print("3. Presentar ventas por rango")
	print("4. Presentar vehículo con mayor venta por semestre")
	print("5. Salir")

	op = int(input("Ingrese opción [1-5]: "))

	if op == 1:
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
			if len(vehiculos) != 0:
				ventas1S = input("Ingrese ventas primer semestre: ")
				ventas1S = ventas1S.split(",")
				while len(ventas1S) != len(vehiculos):
					print("Ingrese la cantidad correcta de valores.")
					ventas1S = input("Ingrese ventas primer semestre: ")
					ventas1S = ventas1S.split(",")
				for i, venta in enumerate(ventas1S):
					ventas1S[i] = int(venta)
			else:
				print("Debes ingresar por lo menos 1 vehículo.")
		elif opSub == 2:
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
			print("Vuelve a ingresar una opción válida.")
	elif op == 3:
		if len(vehiculos) != 0:
			inicio = int(input("Ingrese inicio: "))
			fin = int(input("Ingrese fin: "))

			inicio <= fin

			while inicio > fin or inicio < 0 or fin < 0:
				print("Ingrese valores válidos.")
				inicio = int(input("Ingrese inicio: "))
				fin = int(input("Ingrese fin: "))

			for i, v in enumerate(vehiculos):
				totalV = ventas1S[i] + ventas2S[i]
				if totalV >= inicio and totalV <= fin:
					print("Producto: {} {}".format(v, totalV))
		else:
			print("Debes ingresar por lo menos 1 vehículo")
	elif op == 4:
		# 1er semestre
		ventaMax1S = max(ventas1S)
		vehiculo1S = vehiculos[ventas1S.index(ventaMax1S)]
		# 2do semestre
		ventaMax2S = max(ventas2S)
		vehiculo2S = vehiculos[ventas2S.index(ventaMax2S)]

		print("Producto con mayor venta en semestre 1: {} {}".format(vehiculo1S, ventaMax1S))
		print("Producto con mayor venta en semestre 2: {} {}".format(vehiculo2S, ventaMax2S))	
	elif op == 5:
		salir = True
	else:
		print("Ingrese opción válida.")