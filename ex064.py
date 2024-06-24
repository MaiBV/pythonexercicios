
n = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while n != 999:
    soma += n
    cont += 1
    n = int(input("Digite um número [999 para parar]: "))
print("Foram digitados {} números e a soma entre eles foi {}".format(cont, soma))
print("FIM")
