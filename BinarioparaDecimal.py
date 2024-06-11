def binario_para_decimal(numero_binario):
    """
    Converte um número binário para decimal.


    """

    # Validação completa do número binário
    if not isinstance(numero_binario, str) or not all(c in '01' for c in numero_binario):
        raise ValueError("Número binário inválido. Deve ser uma string contendo apenas '0' e '1'.")

    # Conversão de binário para decimal
    numero_decimal = int(numero_binario, 2)

    # Retorna o valor decimal
    return numero_decimal


# Exemplo de uso
numero_binario = input("Digite um número binário: ")
numero_decimal = binario_para_decimal(numero_binario)
print(f"O valor decimal do número binário {numero_binario} é {numero_decimal}")
