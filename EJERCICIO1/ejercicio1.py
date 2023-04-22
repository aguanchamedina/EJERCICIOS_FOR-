print("----------------------------------")
print("-----------PAR IMPAR--------------")
print("----------------------------------")

# INPUT
while True:
    n = int(input("Ingrese el número de elementos a leer: "))
    if n == 0:
        break
        
    pares = 0
    impares = 0
    
# PROCESS 
    for i in range(n):
        num = int(input("Ingrese un número entero: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
            
    print("Cantidad de números pares: ", pares) # OUTPUT
    print("Cantidad de números impares: ", impares) # OUTPUT


