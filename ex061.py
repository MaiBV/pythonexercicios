print("=" * 30)
print("      10 TERMOS DE UMA PA      ")
print("=" * 30)
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{}".format(termo), end=" º ")
    termo += razao
    cont += 1
print("\nFIM")
