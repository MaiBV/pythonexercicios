soma = 0
cont = 0
for c in range(3, 501, 6):  # if c % 3 == 0:
    cont += 1
    soma += c
    print(c, end=" ")
print("\nA soma de todos os {} valores múltiplos de 3 é {}".format(cont, soma))
print("FIM")
