print("-=" * 20)
print("        Analizador de Triângulos       ")
print("-=" * 20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro seguimento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima PODEM FORMAR um Triângulo!")
    if r1 == r2 == r3:
        print("O triângulo é EQUILÁTERO")
    elif r1 == r2 or r1 == r3 or r3 == r2:
        print("O triângulo é ISÓSCELES")
    elif r1 != r2 != r3 != r1:
        print("O triângulo é ESCALENO")
else:
    print("Os seguimentos acima NÃO PODEM FORMAR Triângulo.")
