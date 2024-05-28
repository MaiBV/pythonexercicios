def hexadecimal_para_decimal(numero_hexadecimal):
  """
  Converte um número hexadecimal para decimal usando a função int().

  Argumentos:
    numero_hexadecimal: Uma string que representa o número hexadecimal a ser convertido.

  Retorno:
    Um inteiro que representa o valor decimal do número hexadecimal.
  """

  # Remove o prefixo "0x" (se houver)
  if numero_hexadecimal.startswith("0x"):
    numero_hexadecimal = numero_hexadecimal[2:]

  # Converte o número hexadecimal para decimal usando int(base=16)
  valor_decimal = int(numero_hexadecimal, base=16)

  return valor_decimal

# Exemplo de uso
numero_hexadecimal = input("Digite um número hexadecimal: ")
valor_decimal = hexadecimal_para_decimal(numero_hexadecimal)
print(f"O valor decimal do número hexadecimal {numero_hexadecimal} \033[35mbase16\033[m é {valor_decimal} \033[35mbase10")
