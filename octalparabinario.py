def octal_para_binario(numero_octal):
    """
    Converte um número octal para binário usando validação completa e conversão individual de dígitos.

    Argumentos:
        numero_octal: um inteiro que representa o número octal a ser convertido.

    Retorno:
        Uma string que representa o valor binário do número octal.
    """

    # Validação completa do número octal
    if not isinstance(numero_octal, int) or numero_octal < 0:
        raise ValueError("Número octal inválido. Deve ser um inteiro não negativo.")

    # Caso especial para o número 0
    if numero_octal == 0:
        return "0"

    # Mapeamento dos dígitos octais para binários
    mapa_octal_binario = {
        0: "000",
        1: "001",
        2: "010",
        3: "011",
        4: "100",
        5: "101",
        6: "110",
        7: "111"
    }

    # Converte cada dígito octal para binário individualmente
    numero_binario = ""
    while numero_octal > 0:
        digito_octal = numero_octal % 10
        numero_octal //= 10
        digito_binario = mapa_octal_binario[digito_octal]
        numero_binario = digito_binario + numero_binario

    # Remove zeros à esquerda, se houver
    numero_binario = numero_binario.lstrip('0')

    # Retorna o valor binário completo
    return numero_binario
# Exemplo de uso
numero_octal = int(input("Digite um número octal: "))
numero_binario = octal_para_binario(numero_octal)
print(f"O valor binário do número octal {numero_octal} é {numero_binario} base2")
