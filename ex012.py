p = float(input('Qual o preço do produto? R$'))
q = p - (p * 5)/100
print("O produto custa {:.2f} R$, na promoção com desconto de 5% vai custar {:.2f} R$".format(p, q))
