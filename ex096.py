def linha():
    print('-' * 40)


def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg}m X {comp}m é de {a}m²')


linha()
print('         CONTROLE DE TERRENOS        ')
linha()
largura = float(input('Qual a largura do terreno (m)? '))
comprimento = float(input('Qual o comprimento do terreno (m)? '))
area(largura, comprimento)
