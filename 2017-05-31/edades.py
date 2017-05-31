# Pida la edad al usuario y determine
# de acuerdo al rango su nominación:

# Rango -> Nominación
# 0 - 11 -> Niño
# 12 - 17 -> Adolescente
# 18 - 30 -> Joven
# 31 - 44 -> Adulto
# 45 - 64 -> Maduro
# 65 - -> Tercera edad

edad = int(input("Ingrese edad: "))
if edad < 12:
	print("Niño")
elif edad < 18:
	print("Adolescente")
elif edad < 31:
	print("Joven")
elif edad < 45:
	print("Adulto")
elif edad < 65:
	print("Maduro")
else:
	print("Tercera edad")
