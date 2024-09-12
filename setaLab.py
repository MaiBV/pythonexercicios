# Solicita ao usuário o comprimento das pernas do triângulo
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))

# Calcula a hipotenusa usando o Teorema de Pitágoras
hypo = (leg_a**2 + leg_b**2) ** 0.5

# Exibe o comprimento da hipotenusa com duas casas decimais
print(f"O comprimento da hipotenusa é {hypo:.2f}")
