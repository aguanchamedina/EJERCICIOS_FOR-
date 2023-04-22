print("-----------------------------------")
print("--------------FACTORIAL------------")
print("-----------------------------------")


# INPUT 
num = int(input("Digite un número: "))

# PROCESS 
if num == 0:
    num = 1
else:
    for i in range(1, num):
        num = num * i

# OUTPUT 
print("Su factorial es:", num)