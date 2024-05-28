from datetime import date

nasc = int(input("Em que ano você nasceu? "))
atual = date.today().year
idade = atual - nasc
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("Sua categoria é a MIRIM.")
elif 9 < idade <= 14:
    print("Categoria INFANTIL.")
elif 14 < idade <= 19:
    print("Sua categoria é a JÚNIOR.")
elif 19 < idade <= 25:
    print("Sua categoria é a SÊNIOR.")
else:  # acima de 25 anos
    print("Sua categoria é a MASTER.")
