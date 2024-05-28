def binario_para_hexadecimal(numero_binario):
    """
    Converte um número binário para hexadecimal.

    Argumentos:
        numero_binario: Uma string que representa o número binário a ser convertido.

    Retorno:
        Uma string que representa o valor hexadecimal do número binário.
    """

    # Validação completa do número binário
    if not isinstance(numero_binario, str) or not all(c in '01' for c in numero_binario):
        raise ValueError("Número binário inválido. Deve ser uma string contendo apenas '0' e '1'.")

    # Remove zeros à esquerda, se houver
    numero_binario = numero_binario.lstrip('0')

    # Caso especial para o número 0
    if not numero_binario:
        return "0"

    # Padroniza o número binário para ser múltiplo de 4 bits, adicionando zeros à esquerda se necessário
    while len(numero_binario) % 4 != 0:
        numero_binario = '0' + numero_binario

    # Mapeamento dos grupos de 4 bits para dígitos hexadecimais
    mapa_binario_hexadecimal = {
        '0000': '0',
        '0001': '1',
        '0010': '2',
        '0011': '3',
        '0100': '4',
        '0101': '5',
        '0110': '6',
        '0111': '7',
        '1000': '8',
        '1001': '9',
        '1010': 'A',
        '1011': 'B',
        '1100': 'C',
        '1101': 'D',
        '1110': 'E',
        '1111': 'F'
    }

    # Converte cada grupo de 4 bits para o dígito hexadecimal correspondente
    numero_hexadecimal = ""
    for i in range(0, len(numero_binario), 4):
        grupo_binario = numero_binario[i:i+4]
        numero_hexadecimal += mapa_binario_hexadecimal[grupo_binario]

    # Retorna o valor hexadecimal completo
    return numero_hexadecimal

# Exemplo de uso
numero_binario = input("Digite um número binário: ")
numero_hexadecimal = binario_para_hexadecimal(numero_binario)
print(f"O valor hexadecimal do número binário {numero_binario} é {numero_hexadecimal}")
