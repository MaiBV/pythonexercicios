from time import sleep


def lin():
    print('-+' * 30)


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')


lin()
contador(1, 10, 1)
lin()
contador(0, 100, 10)
lin()
contador(10, 0, 2)
lin()
contador(10, 0, 2)
lin()
contador(-5, 15, 5)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)