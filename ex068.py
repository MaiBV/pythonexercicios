from random import randint
v = 0
print("=-" * 40)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 40)
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("PAR OU ÍMPAR? [P/I] ")).upper().strip()[0]
    print("-" * 80)
    print(f"VOCÊ JOGOU {jogador} E O COMPUTADOR JOGOU {computador}. TOTAL DE {total} ", end="")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 ==0:
            print("VOCÊ VENCEU!")
            v += 1
        else:
            print("VOCÊ PERDEU!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("VOCÊ VENCEU!")
        else:
            print("VOCÊ PERDEU!")
            break
    print("Vamos jogar novamente...")
print( f"GAME OVER! Você venceu {v} vezes." )
print("-" * 80)
print("=-" * 40)
