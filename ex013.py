sal = float(input('Qual o salário do Funcionário? R$ '))
salr = sal + (sal * 15) / 100
print('Um funcionário que recebia {:.2f}R$, com 15% de aumento, passa a receber {:.2f} R$'.format(sal, salr))
