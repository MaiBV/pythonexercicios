n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
n = n1 - n2
m = n1 * n2
di = n1 // n2
d = n1 / n2
e = n1 ** n2

print('A soma é {}, \no produto é {}, a divisão é {:.2f}'.format(s, m, d), end=' ')
print('A divisão inteira vale {}, e a potência {}'.format(di, e))
