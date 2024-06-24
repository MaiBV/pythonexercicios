while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print( "-" * 37)
    if n < 0:
        break
    for c in range(1, 11):
        print(f"{n} X {c} = {n * c}")
    print("-" * 37)
print("PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!")
