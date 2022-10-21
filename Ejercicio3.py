
""" Ejercicio 3

imprimir los primeros 20 números primos

"""

vNumeroRevisar = 2
vNumerosPrimos = 0

while vNumerosPrimos < 20:
    vEsPrimo = 1
    for i in range(2, vNumeroRevisar):  
        if vNumeroRevisar % i == 0: 
            vEsPrimo=0
    
    if vEsPrimo == 1:
        print(vNumeroRevisar)
        vNumerosPrimos = vNumerosPrimos+1
    
    vNumeroRevisar = vNumeroRevisar+1

