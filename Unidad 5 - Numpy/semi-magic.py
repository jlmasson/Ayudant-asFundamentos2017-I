# -*- coding: utf-8 -*-

#
#Autor: Madelyne Velasco
#

from numpy import*
from random import randint

# Un cuadrado semi-mágico es una matriz cuadrada conteniendo números tales que la
#suma las dos diagonales principales producen el mismo resultado.

#Escriba un programa que coloque números enteros aleatorios de una cifra en una matriz
#de 4 filas y 4 columnas. Repita el ciclo hasta que la matriz sea un cuadrado semi-mágico.
#El programa debe mostrar la matriz resultante y la cantidad de intentos que realizó el
#programa hasta llenar la matriz con éxito.

n=int(input('Ingrese el tamano de la matriz'))

w=0
k=1

while w==0:
    z=cuadrados(n)

    cuadrado=zeros([n,n],int)
    for i in range (n):
        for j in range (n):
            cuadrado[i,j]=randint(0,9)

    sum1=0
    sum2=0

    for i in range (1,n) :
        sum1=sum1+cuadrado[i,i]
        sum2=sum2+cuadrado[i,n-i]

    if sum1==sum2:
        w=1
        print(cuadrado)
        print('Se encontro un cuadrado semi magico en ', k, ' intentos ')
    else:
        k=k+1
