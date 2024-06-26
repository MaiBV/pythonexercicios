cont = ("zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove",
        "dez", "onze", "doze", "treze", "quatorze",
        "quinze", "dezesseis", "dezessete", "dezoito",
        "dezenove", "vinte")

while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if 0 <= num <= 20:
            break
        print("Tente novamente.", end=" ")
    print(f"Você digitou o número {cont[num]}")

    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
        print("Resposta inválida. Tente novamente.")

    if resp == "N":
        print("Até logo!")
        break

# Explicação:
#
# O código agora tem dois loops while True aninhados.
# O primeiro loop while True é usado para garantir que o usuário digite um número entre 0 e 20.
# Após digitar o número, o programa imprime a tradução do número em português.
# Em seguida, o segundo loop while True é usado para perguntar se o usuário deseja continuar.
# Se a resposta for "N", o programa imprime "Até logo!" e sai do loop externo com o break.
# Se a resposta for "S", o programa volta ao início do loop externo e pergunta novamente pelo número.
# Isso continua até que o usuário escolha sair digitando "N".