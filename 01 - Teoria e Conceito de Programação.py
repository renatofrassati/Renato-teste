#exercicio 1
valor_da_casa = float(input("Valor da casa: R$ "))
salario = float(input("Meu salário: R$ "))
ano_pagamento = int(input("Quantos anos para pagamento: "))
prestacao = valor_da_casa / (ano_pagamento * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de R$: {valor_da_casa:.2f}, meu salário é R$: {salario:.2f}, e irei pagar em {ano_pagamento} anos")
if prestacao <= minimo:
    print("O emprestimo é concedido")
else:
    print("o emprestimo é negado")