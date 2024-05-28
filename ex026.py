frase = str(input("Digite uma frase: ")).strip().upper()
print("A letra A apareceu {} vezes na frase".format(frase.count('A')))
print('A primeira letra A apareceu no posição {}'.format(frase.find('A')+1))
print('A última A apareceu na posição {}'.format(frase.rfind('A')+1))
