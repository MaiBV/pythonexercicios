num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input("Sua opçãp: "))
if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")

