velocidade = float(input("Qual a velocidade atual do carro? "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print("Você foi multado. A multa vai custar em {:.2f} R$".format(multa))
print("Tenha um bom dia! Dirija com segurança.")

