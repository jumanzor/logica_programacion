
""" Ejercicio 4

imprimir un triángulo de asteriscos de una 
altura definida en una variable

ejemplo

altura=10

*
**
***
****
*****
******
*******
********
*********
**********

"""

vAltura=10

for i in range(1, vAltura+1):  
  for j in range(1, i+1):
    print("*", end=" ")
  print("")
