# -*- coding: utf-8 -*-

#
#Autor: Madelyne Velasco
#

"""
Crea un arreglo de la lista  [2, 3.2, 5.5, -6.4, -2.2, 2.4] a y asígnalo a la variable a
"""

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])

"""
¿Qué va a dar a[1]
"""
print a[1]
#3.2

"""
¿Qué va a dar a[1:4]?
"""
print a[1:4]
#[ 3.2 5.5 -6.4]

"""
Crea un arreglo de dos dimensiones con 
[[2, 3.2, 5.5, -6.4, -2.2, 2.4],
[1, 22, 4, 0.1, 5.3, -9],
[3, 1, 2.1, 21, 1.1, -2]]
"""
a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
 [1, 22, 4, 0.1, 5.3, -9],
 [3, 1, 2.1, 21, 1.1, -2]])

"""
¿Puedes adivinar qué es lo que devuelve lo siguiente?
a[:, 3]
a[1:4, 0:4]
a[1:, 2]
"""
print a[:, 3]
#[ -6.4 0.1 21. ]

print a[1:4, 0:4]
#[[ 1. 22. 4. 0.1]
#[ 3. 1. 2.1 21. ]]

print a[1:, 2]
#[ 4. 2.1]