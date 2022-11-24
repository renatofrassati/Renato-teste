#exercicio 2
peso = float(input("Meu peso é: (kg) "))
altura = float(input("Minha altura é: (m) "))
imc = peso / (altura ** 2)
print(f"Seu imc é de : {imc:.1f} ")
if imc < 18.5:
    print("vc esta abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("vc esta com peso ideal")
elif imc >= 25 and imc < 30:
    print("vc esta em sobrepeso")
elif imc >= 30 and imc < 40:
    print("vc esta obeso")
elif imc >= 40:
    print(("vc esta com obesidade morbida"))