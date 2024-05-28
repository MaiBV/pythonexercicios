sal = float(input("Qual o seu salário? R$"))
if sal > 1250:
    novo = sal + (sal * 10 / 100)
    print("Seu aumento será de R${:.2f}".format(sal * 10 / 100))

else:
    novo = sal + (sal * 15 / 100)
    print("Seu aumento será de R${:.2f}".format(sal * 15 / 100))
print("Quem ganhava R${:.2f} passará a ganhar R${:.2f}".format(sal, novo))

