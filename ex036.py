casa = float(input("Qual o valor da imóvel?R$ "))
salario = float(input("Quanto recebe o comprador?R$ "))
anos = int(input("Em quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = (salario * 30) / 100
print("Para pagar um imóvel de R${:.2f} em {} anos".format(casa, anos), end='')
print(" a prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print("Empréstimo CONCEDIDO")
else:
    print("Empréstimo NÃO CONCEDIDO")

