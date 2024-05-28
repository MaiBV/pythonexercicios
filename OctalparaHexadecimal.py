def octal_para_binario(numero_octal):
    """
    Converte um número octal para binário.

    Argumentos:
        numero_octal: Um inteiro que representa o número octal a ser convertido.

    Retorno:
        Uma string que representa o valor binário do número octal.
    """

    # Validação completa do número octal
    if not isinstance(numero_octal, int) or any(d not in '01234567' for d in str(numero_octal)):
        raise ValueError("Número octal inválido. Deve ser um inteiro contendo apenas dígitos de 0 a 7.")

    # Mapeamento dos dígitos octais para binários
    mapa_octal_binario = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }

    # Converte cada dígito octal para o dígito binário correspondente
    numero_binario = "".join(mapa_octal_binario[d] for d in str(numero_octal))

    # Remove zeros à esquerda, se houver
    numero_binario = numero_binario.lstrip('0')

    # Retorna o valor binário completo
    return numero_binario if numero_binario else '0'


def binario_para_hexadecimal(numero_binario):
    """
    Converte um número binário para hexadecimal.

    Argumentos:
        numero_binario: Uma string que representa o número binário a ser convertido.

    Retorno:
        Uma string que representa o valor hexadecimal do número binário.
    """

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
    numero_hexadecimal = "".join(
        mapa_binario_hexadecimal[numero_binario[i:i + 4]] for i in range(0, len(numero_binario), 4))

    # Retorna o valor hexadecimal completo
    return numero_hexadecimal


def octal_para_hexadecimal(numero_octal):
    """
    Converte um número octal para hexadecimal.

    Argumentos:
        numero_octal: Um inteiro que representa o número octal a ser convertido.

    Retorno:
        Uma string que representa o valor hexadecimal do número octal.
    """

    numero_binario = octal_para_binario(numero_octal)
    numero_hexadecimal = binario_para_hexadecimal(numero_binario)
    return numero_hexadecimal


# Exemplo de uso
numero_octal = int(input("Digite um número octal: "))
numero_hexadecimal = octal_para_hexadecimal(numero_octal)
print(f"O valor hexadecimal do número octal {numero_octal} é {numero_hexadecimal}")
