conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9, 10}
conjunto_uniao = conjunto.union(conjunto2)
print(f'Conjunto união: {conjunto_uniao}')
conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Conjunto intersecção: {conjunto_interseccao}')
conjunto_diferenca = conjunto.difference(conjunto2)
print(f'Conjunto diferenção: {conjunto_diferenca}')
conjunto_diferenca1 = conjunto2.difference(conjunto)
print(f'Conjunto diferença1: {conjunto_diferenca1}')
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
# menos numeral 5 porque tem nos dois conjuntos
print(f'Conjunto diferença simétrica: {conjunto_diff_simetrica}')

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(f'B é subconjunto de A: {conjunto_subset}')
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(f'A é subconjunto de B: {conjunto_subset}')
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(f'B é um superconjunto de A: {conjunto_superset}')

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)