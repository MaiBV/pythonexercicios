n = int(input(" Digite um número: "))
print("-=" * 12)
for c in range(0, 11):
    print("{} X {:2} = {}".format(n, c, n * c))
print("=-" * 12)
