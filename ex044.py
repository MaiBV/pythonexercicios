print(f'{" LOJAS GUANABARA ":=^40}')
preco = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão ''')
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2X de {:.2f} R$".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Em quantas vezes você vai parcelar? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}X de {:.2f} R$ COM JUROS".format(totparc, parcela))
else:
    total = preco
    print("Opção inválida de pagamento. Escolha uma das opções acima.")
print("Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final".format(preco, total))
