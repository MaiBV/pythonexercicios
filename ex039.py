from datetime import date

atual = date.today().year
nasc = int(input("Em que ano você nasceu? "))
sexo_biologico = str(input("Qual o seu sexo biológico - M ou F? ")).upper()
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18 and sexo_biologico == 'M':
    print("Você tem que se alistar IMEDIATAMENTE.")
elif idade < 18 and sexo_biologico == 'M':
    saldo = 18 - idade
    print("Você ainda não tem 18 anos. Falta(m) {} ano(s) para seu alistamento.".format(saldo))
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))
elif idade > 18 and sexo_biologico == 'M':
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} ano(s).".format(saldo))
    ano = atual - saldo
    print("Seu alistamento sería em {}".format(ano))
else:  # sexo == F:
    print("O seu alistamento não é obrigatório.")
