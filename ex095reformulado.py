jogadores = []

def cadastrar_jogador():
    jogador = {}
    jogador['nome'] = input('Nome do Jogador: ')
    while True:
        try:
            tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
            if tot <= 0:
                print('Erro! O número de partidas deve ser maior que 0.')
                continue
            break
        except ValueError:
            print('Erro! O número de partidas deve ser um número inteiro.')
    partidas = []
    for c in range(tot):
        while True:
            try:
                gols = int(input(f'   Quantos gols na partida {c + 1}? '))
                partidas.append(gols)
                break
            except ValueError:
                print('Erro! O número de gols deve ser um número inteiro.')
    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())

def mostrar_jogadores():
    print('-=' * 30)
    print('cod ', end='')
    for i in jogadores[0].keys():
        print(f'{i:<15}', end='')
    print()
    print('-=' * 40)
    for k, v in enumerate(jogadores):
        print(f'{k + 1:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
    print('-=' * 40)

def buscar_jogador():
    while True:
        try:
            busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
            if busca == 999:
                break
            if busca > len(jogadores):
                print(f'ERRO! Não existe jogador com código {busca}!')
                continue
            jogador = jogadores[busca - 1]
            print(f' --LEVANTAMENTO DO JOGADOR {jogador["nome"]}: ')
            for i, g in enumerate(jogador['gols']):
                print(f'    No jogo {i + 1} fez {g} gols')
            print('-' * 40)
        except ValueError:
            print('Erro! O código do jogador deve ser um número inteiro.')

while True:
    cadastrar_jogador()
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

mostrar_jogadores()
buscar_jogador()

print('<< VOLTE SEMPRE >>')