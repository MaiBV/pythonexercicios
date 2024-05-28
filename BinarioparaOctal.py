def binario_para_octal(numero_binario):
    """
    Converte um número binário para octal.

    Argumentos:
        numero_binario: Uma string que representa o número binário a ser convertido.

    Retorno:
        Uma string que representa o valor octal do número binário.
    """

    # Validação completa do número binário
    if not isinstance(numero_binario, str) or not all(c in '01' for c in numero_binario):
        raise ValueError("Número binário inválido. Deve ser uma string contendo apenas '0' e '1'.")

    # Remove zeros à esquerda, se houver
    numero_binario = numero_binario.lstrip('0')

    # Caso especial para o número 0
    if not numero_binario:
        return "0"

    # Padroniza o número binário para ser múltiplo de 3 bits, adicionando zeros à esquerda se necessário
    while len(numero_binario) % 3 != 0:
        numero_binario = '0' + numero_binario

    # Mapeamento dos grupos de 3 bits para dígitos octais
    mapa_binario_octal = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7'
    }

    # Converte cada grupo de 3 bits para o dígito octal correspondente
    numero_octal = ""
    for i in range(0, len(numero_binario), 3):
        grupo_binario = numero_binario[i:i+3]
        numero_octal += mapa_binario_octal[grupo_binario]

    # Retorna o valor octal completo
    return numero_octal

# Exemplo de uso
numero_binario = input("Digite um número binário: ")
numero_octal = binario_para_octal(numero_binario)
print(f"O valor octal do número binário {numero_binario} é {numero_octal}")
