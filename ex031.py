d = float(input("Qual a distância da viagem? "))
if d <= 200:
    print("O preço da passagem custa {:.2f} R$".format(d * 0.50))
else:
    print("O Preço da passagem custa {:.2f} R$".format(d * 0.45))  # Melhor opção utilizada

'''preco = d * 0.5 if d <= 200 else d * 0.45
print("Sua passagem custou {} R$".format(preco))'''  # Opção simplificada



