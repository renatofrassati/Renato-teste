#exercicio 7 - referente ao 35
numero = soma = 0
while numero != 999:
    numero = int(input("Digite um numero: "))
    if numero == 999:
        break
    soma += numero
#print("A soma vale {}". format(soma))
print(f"A soma vale {soma}")