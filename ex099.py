from time import sleep


def lin():
    print('-=' * 30)


def maior(* num):
    cont = maior = 0
    print('Analizando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end=' ')
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


lin()
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()
maior()