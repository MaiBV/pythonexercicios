peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura ** 2)
print("Seu IMC é {:.1f}".format(imc))
if imc < 18.5:
    print("ABAIXO DO PESO.")
elif 18.5 <= imc < 25:
    print("PESO IDEAL.")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 <= imc <= 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MÓRBIDA")
