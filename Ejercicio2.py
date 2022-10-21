''' Ejercicio 2

Escribir un programa que imprima los numeros del 1 al 100
pero, debe cambiar el número según estas reglas:
-- si es multiplo de 3 debe imprimir FIZZ
-- si es multiplo de 5 debe imprimir BUZZ
-- si es multiplo de 3 y 5 a la vez, debe imprimir FIZZBUZZ

'''



# forma incorrecta de programarlo 


for i in range (1,101):
    if i%3 == 0:
        print("FIZZ")
    elif i%5 == 0:
        print("BUZZ")
    elif i%3 == 0 and i%5 == 0:
        print("FIZZBUZZ")
    else:
        print(i)

