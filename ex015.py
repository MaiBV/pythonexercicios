dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
print('O total a pagar é de {:.2f} R$'.format((60 * dias) + (0.15 * km)))
