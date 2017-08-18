def dibujar_linea(width, edge, filling):
	print(filling.join([edge] * (width + 1)))


def mostrar_ganador(player):
	if player == 0:
		print("Tie")
	else:
		print("Player " + str(player) + " wins!")

def revisar_ganador_fila(row):
	"""
	Return the player number that wins for that row.
	If there is no winner, return 0.
	"""
	if row[0] == row[1] and row[1] == row[2]:
		return row[0]
	return 0

def get_columna(game, col_number):
	return [game[x][col_number] for x in range(3)]

def get_fila(game, row_number):
	return game[row_number]

def revisar_ganador(game):
	game_slices = []
	for index in range(3):
		game_slices.append(get_fila(game, index))
		game_slices.append(get_columna(game, index))

	# check diagonals
	down_diagonal = [game[x][x] for x in range(3)]
	up_diagonal = [game[0][2], game[1][1], game[2][0]]
	game_slices.append(down_diagonal)
	game_slices.append(up_diagonal)

	for game_slice in game_slices:
		winner = revisar_ganador_fila(game_slice)
		if winner != 0:
			return winner

	return winner

def iniciar_juego():
	return [[0, 0, 0] for x in range(3)]

def mostrar_juego(game):
	d = {2: "O", 1: "X", 0: "_"}
	dibujar_linea(3, " ", "_")
	for row_num in range(3):
		new_row = []
		for col_num in range(3):
			new_row.append(d[game[row_num][col_num]])
		print("|" + "|".join(new_row) + "|")


def add_pieza(game, player, row, column):
	"""
	game: game state
	player: player number
	row: 0-index row
	column: 0-index column
	"""
	game[row][column] = player
	return game

def revisar_vacio(game, row, column):
	return game[row][column] == 0

def transformar_coordenada(user_input):
	return user_input - 1

def cambiar_jugador(player):
	if player == 1:
		return 2
	else:
		return 1

def verificar_movimiento(game):
	for row_num in range(3):
		for col_num in range(3):
			if game[row_num][col_num] == 0:
				return True
	return False

if __name__ == '__main__':
	game = iniciar_juego()
	mostrar_juego(game)
	player = 1
	winner = 0  # the winner is not yet defined

	# go on forever
	while winner == 0 and verificar_movimiento(game):
		print("Currently player: " + str(player))
		available = False
		while not available:
			row = transformar_coordenada(int(input("Which row? (start with 1) ")))
			column = transformar_coordenada(int(input("Which column? (start with 1) ")))
			available = revisar_vacio(game, row, column)
		game = add_pieza(game, player, row, column)
		mostrar_juego(game)
		player = cambiar_jugador(player)
		winner = revisar_ganador(game)
	mostrar_ganador(winner)