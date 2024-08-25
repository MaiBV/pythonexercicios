# import moeda
#
# p = float(input('Digite o preço: R$ '))
# print(f'A metade de R${p} é R${moeda.metade(p)}')
# print(f'O dobro de R${p} é R${moeda.dobro(p)}')
# print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
# print(f'Diminuindo 12%, temos R${moeda.diminuir(p, 12)}')


from moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${metade(p)}')
print(f'O dobro de R${p} é R${dobro(p)}')
print(f'Aumentando 10%, temos R${aumentar(p, 10)}')
print(f'Diminuindo 12%, temos R${diminuir(p, 12)}')
