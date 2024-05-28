def hexadecimal_para_binario(numero_hexadecimal):
    """
    Converte um número hexadecimal para binário.

    Argumentos:
        numero_hexadecimal: Uma string que representa o número hexadecimal a ser convertido.

    Retorno:
        Uma string que representa o valor binário do número hexadecimal, sem os dois primeiros dígitos.
    """

    # Validação completa do número hexadecimal
    if not isinstance(numero_hexadecimal, str) or not all(c in '0123456789ABCDEFabcdef' for c in numero_hexadecimal):
        raise ValueError("Número hexadecimal inválido. Deve ser uma string contendo apenas caracteres válidos de 0-9, A-F, a-f.")

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

    # Remove os dois primeiros dígitos do resultado binário
    #numero_binario = numero_binario[2:]

    # Retorna o valor binário completo, sem os dois primeiros dígitos
    return numero_binario

# Exemplo de uso
numero_hexadecimal = input("Digite um número hexadecimal: ")
numero_binario = hexadecimal_para_binario(numero_hexadecimal)
print(f"O valor binário do número hexadecimal {numero_hexadecimal} é {numero_binario}")
