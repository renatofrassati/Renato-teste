#exercicio 6 - referente ao 29
#from math import factorial
#numero = int(input("Numero para calcular o factorial: "))
#f = factorial(numero)
#print(f"O factorial de {numero} é {f}")
#print("O factorial de {} é {}".format(numero, f))

numero = int(input("Numero para calcular o factorial: "))
c = numero
factorial = 1
while c > 0:
    print(f"{c}",end="")
    print(" x " if c > 1 else " = ", end="")
    factorial *= c
    c -= 1
#print(f"{factorial} ")
print("{}" .format(factorial))