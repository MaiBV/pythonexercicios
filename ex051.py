print("=" * 30)
print("      10 TERMOS DE UMA PA      ")
print("=" * 30)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10) * razao
for c in range(primeiro, decimo, razao):
    print("{}".format(c), end=" º ")
print("\nACABOU")




