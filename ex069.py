print("-" * 50)
print("              CADASTRE UMA PESSOA              ")
print("-" * 50)
tot18 = totalhomens = totalmulheres20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totalhomens += 1
    if sexo == "F" and idade < 20:
        totalmulheres20 += 1
    print("-" * 50)
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"Ao todo temos {totalhomens} homens cadastrados")
print(f"E temos {totalmulheres20} mulheres com menos de 20 anos")
print("-" * 50)


