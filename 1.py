tipo = input("Digite o tipo de combustível (A- Álcool ou G- Gasolina): ")
qtlitros = float(input("Digite a quantidade de litros abastecidos : "))

if tipo == "A":
    if qtlitros <= 20:
        print("total a pagar: R$", qtlitros * (2.9 * 0.03))
    else:
        print("total a pagar: R$", qtlitros * (2.9 * 0.05))
elif tipo == "G":
    if qtlitros <= 20:
        print("total a pagar: R$", qtlitros * (3.35 * 0.04))
    else:
        print("total a pagar: R$", qtlitros * (3.35 * 0.06))
else:
    print("Opção inválida")
