valores = []
mai = men = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        mai = men = valores[v]
    else:
        if valores[v] > mai:
            mai = valores[v]
        if valores[v] < men:
            men = valores[v]
print('=-' * 40)
print(f'\nVocê digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
