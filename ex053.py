def inverter_frase(frase):
  """
  Função para inverter uma frase.

  Argumentos:
    frase (str): A frase a ser invertida.

  Retorno:
    str: A frase invertida.
  """
  return " ".join(frase.split()[::-1])

def verificar_palindromo(frase):
  """
  Função para verificar se uma frase é um palíndromo.

  Argumentos:
    frase (str): A frase a ser verificada.

  Retorno:
    bool: True se a frase for um palíndromo, False caso contrário.
  """
  frase_sem_espaco = frase.replace(" ", "").lower()
  return frase_sem_espaco == frase_sem_espaco[::-1]

frase = str(input("Digite uma frase: ")).strip()

frase_invertida = inverter_frase(frase)
print(f"O inverso de {frase} é {frase_invertida}")

if verificar_palindromo(frase):
  print("A frase é um palíndromo!")
else:
  print("Esta frase não é um palíndromo.")
