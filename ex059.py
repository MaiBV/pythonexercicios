from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input("***** Qual é a sua opção? "))
    sleep(2)
    if opcao == 1:
        soma = n1 + n2
        print("\033[32mA soma de {} + {} é {}\033[m".format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print("\033[32mA multiplicação de {} X {} é {}\033[m".format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("\033[32mEntre {} e {} o maior valor é {}\033[m".format(n1, n2, maior))
    elif opcao == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida")
    print("=-=" * 10)
    sleep(2)
print("Fim do programa! Volte sempre!")
