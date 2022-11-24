#exercicio 3 - referente ao 8

from datetime import date
atual = date.today().year
ano_nascimento = int(input("Ano de nascimento: "))
idade = atual - ano_nascimento
print(f"O atleta tem {idade} anos")
if idade <= 9:
    print("A categoria é mirim")
elif idade <= 14:
    print("A categoria é infantil")
elif idade <= 19:
    print("A categoria é junior")
elif idade <= 25:
    print("A categoria é senior")
else:
    print("A categoria é master")
