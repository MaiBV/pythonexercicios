from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print("-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-")
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-")
jogador = int(input("Em que número eu pensei? ")) #jogador tenta adivinhar
print("PROCESSANDO...")
sleep(3)
if jogador == computador:
    print("Parabéns você adivinhou!")
else:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(computador, jogador))

