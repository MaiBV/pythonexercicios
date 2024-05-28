def octal_para_decimal(numero_octal):
  """
  Converte um número octal para decimal.

  Argumentos:
    numero_octal: Uma string que representa o número octal a ser convertido.

  Retorno:
    Um inteiro que representa o valor decimal do número octal.
  """

  # Verifica se o número octal é válido
  if not numero_octal.isdigit() or any(char in numero_octal for char in "abcdefg"):
    raise ValueError("Número octal inválido.")

  # Converte o número octal para uma lista de dígitos
  digitos_octal = list(numero_octal)

  # Inicializa a variável que armazenará o valor decimal
  valor_decimal = 0

  # Multiplica cada dígito octal pela potência de 8 correspondente e soma ao valor decimal
  for i, digito in enumerate(digitos_octal[::-1]):
    valor_decimal += int(digito) * 8 ** i

  return valor_decimal

# Exemplo de uso
numero_octal = input("Digite um número octal: ")
valor_decimal = octal_para_decimal(numero_octal)
print(f"O valor decimal do número octal {numero_octal} \033[32mbase8\033[m é {valor_decimal} \033[32mbase10")
