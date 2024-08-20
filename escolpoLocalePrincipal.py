'''def teste(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')'''


def funcao():
    n1 = 4
    print(f'N1 local vale {n1}')


n1 = 2
funcao()
print(f'N1 global vale {n1}')