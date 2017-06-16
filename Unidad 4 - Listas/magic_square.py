#
#Autor: Madelyne Velasco
#

"""
Johnny diseñó un cuadrado mágico (un cuadrado que sus columnas, filas y diagonales suman igual) y te han pedido un programa para probarlo. 
La primera entrada que te darán es el tamaño del cuadrado y las siguientes líneas serán las filas del cuadrado con los elementos de cada fila separadas por un espacio entre sí. 
La salida del programa será lo siguiete:
-La primera línea será el número de líneas que no suman la primera diagonal. Si el cuadrado es mágico, esto devolverá un cero. 
-Las siguientes líneas mostrarán las columnas y filas que no sumen a la diagonal principal. Las filas van desde 1 a n y las columnas de -1 a -n y la antidiagonal se la coloca como cero. 

Ej entrada:
4 
16 3 2 13 
5 10 11 8 
6 9 7 12 
4 15 14 1

Ej salida:
3 
-2 
-1 
0
"""

start = ''
i = 0
entrada = []
array = []
diag_main = 0
diag_no = 0
x = 0
z = 0

n = int(input('Ingresa el tamaño de N'))
for y in range(0, n):
	entrada.append(input('Ingresa tu fila'))

for line in entrada:
    line = str(line)
    res = line.strip
    res = line.split(' ')
    res = [int(i) for i in res]
    array.append(res)
    diag_main = int(res[z]) + diag_main
    diag_no = int(res[size-z-1]) + diag_no
    z +=1

no_equal= []

##row
tot = 0
for i in range (0, size):
    for j in range(0, size):
        tot = tot + array[i][j]

    if (tot != diag_main):
        no_equal.append(i+1)
    tot = 0

##cols
tot = 0
for j in range (0, size):
    for i in range(0, size):
        tot = tot + array[i][j]
    if (tot != diag_main):
        no_equal.append(-j-1)
    tot = 0

if (diag_main != diag_no):
    no_equal.append(0)

no_equal.sort()
print(len(no_equal))
for i in no_equal:
    print(i)