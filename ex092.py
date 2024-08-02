from datetime import datetime
dados = dict()
while True:
    nome = input('Nome: ')
    if nome.isalpha():
        dados['nome'] = nome
        break
    else:
        print("Por favor, insira apenas letras no nome.")
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 15) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'   - {k} tem o valor {v}')