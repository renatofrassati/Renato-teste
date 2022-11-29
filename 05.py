#exercicio 5 - referente ao 22
from  datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano_nascimento = int(input("Em que ano ela nasceu? "))
    idade = atual - ano_nascimento
    print(f"Essa pessoa tem {idade} anos")
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} maiores de idade" .format(totmaior))
print("Ao todo tivemos {} menor de idade".format(totmenor))