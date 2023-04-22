print("---------------------------------")
print("-----------MULTIPLO--------------")
print("---------------------------------")

# INPUT 
multiplo7 = 0
multiplo9 = 0

# PROCESS 
for i in range(1000, 5001):
    if i % 7 == 0:
        multiplo7 += 1
    if i % 9 == 0:
        multiplo9 += 1

# OUTPUT 
print("Multiplos de 7:", multiplo7)
print("Multiplos de 9:", multiplo9)