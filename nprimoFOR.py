for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)



# a = int(input('Entre com o número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print(f'Número {a} é primo. ')
# else:
#     print(f'Número {a} não é primo.')