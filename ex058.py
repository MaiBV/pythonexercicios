from random import randint

computador = randint(0, 10)

print("sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi? ")
acertou = False
totpalpite = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    totpalpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
        print("ACERTOU!")
print("Foram necessários {} palpites para vencer. Parabéns!".format(totpalpite))
