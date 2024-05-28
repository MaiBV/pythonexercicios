def hexadecimal_para_binario(numero_hexadecimal):
    """
    Converte um número hexadecimal para binário.

    Argumentos:
        numero_hexadecimal: Uma string que representa o número hexadecimal a ser convertido.

    Retorno:
        Uma string que representa o valor binário do número hexadecimal.
    """

    # Validação completa do número hexadecimal
    if not isinstance(numero_hexadecimal, str) or not all(c in '0123456789ABCDEFabcdef' for c in numero_hexadecimal):
        raise ValueError(
            "Número hexadecimal inválido. Deve ser uma string contendo apenas caracteres válidos de 0-9, A-F, a-f.")

    # Mapeamento dos dígitos hexadecimais para binários
    mapa_hexadecimal_binario = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
        'a': '1010',
        'b': '1011',
        'c': '1100',
        'd': '1101',
        'e': '1110',
        'f': '1111'
    }

    # Converte cada dígito hexadecimal para o dígito binário correspondente
    numero_binario = "".join(mapa_hexadecimal_binario[c] for c in numero_hexadecimal)

    # Remove zeros à esquerda, se houver
    numero_binario = numero_binario.lstrip('0')

    # Retorna o valor binário completo
    return numero_binario if numero_binario else '0'


def binario_para_octal(numero_binario):
    """
    Converte um número binário para octal.

    Argumentos:
        numero_binario: Uma string que representa o número binário a ser convertido.

    Retorno:
        Uma string que representa o valor octal do número binário.
    """

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
    numero_octal = "".join(mapa_binario_octal[numero_binario[i:i + 3]] for i in range(0, len(numero_binario), 3))

    # Retorna o valor octal completo
    return numero_octal


def hexadecimal_para_octal(numero_hexadecimal):
    """
    Converte um número hexadecimal para octal.

    Argumentos:
        numero_hexadecimal: Uma string que representa o número hexadecimal a ser convertido.

    Retorno:
        Uma string que representa o valor octal do número hexadecimal.
    """

    numero_binario = hexadecimal_para_binario(numero_hexadecimal)
    numero_octal = binario_para_octal(numero_binario)
    return numero_octal


# Exemplo de uso
numero_hexadecimal = input("Digite um número hexadecimal: ")
numero_octal = hexadecimal_para_octal(numero_hexadecimal)
print(f"O valor octal do número hexadecimal {numero_hexadecimal} é {numero_octal}")
