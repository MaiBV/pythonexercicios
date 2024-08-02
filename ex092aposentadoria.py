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
sexo = str(input('Sexo (M/F): ')).upper()
while sexo not in ['M', 'F']:
    sexo = str(input('Sexo (M/F): ')).upper()
dados['sexo'] = 'Masculino' if sexo == 'M' else 'Feminino'
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    idade_aposentadoria = 65 if sexo == 'M' else 62
    anos_faltantes = idade_aposentadoria - dados['idade']
    if anos_faltantes > 0:
        dados['aposentadoria'] = f'Faltam {anos_faltantes} anos para se aposentar'
    else:
        dados['aposentadoria'] = 'Já pode se aposentar'
print('-=' * 30)
for k, v in dados.items():
    print(f'   - {k}: {v}')