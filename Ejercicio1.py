
""" Ejercicio 1

Programen la secuencia de Fibonacci, los primeros 20 numeros de la secuencia.
La secuencia es asi:
0,1,1,2,3,5,8,13,21,34,55,89,144,233...

Inicia en 0 y 1
Luego cada nuevo numero es la suma de los dos anteriores.
"""

vUno = 0
vDos = 1
vFibonnacci = 0
for i in range(1,21):
    print(vUno)
    vFibonnacci = vUno + vDos
    vUno=vDos
    vDos=vFibonnacci
