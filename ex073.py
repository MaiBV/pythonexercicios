times = ("Flamengo", "Palmeiras SP", "Bahia", "Botafogo FR RJ",
         "CA Paranaense PR", "Red Bull Bragantino SP", "Internacional RS",
         "Cruzeiro", "São Paulo FC SP", "Atlético Mineiro MG", "Fortaleza CE",
         "EC Juventude RS", "Criciúma", "Cuiabá Esporte Clube MT", "Vasco Gama",
         "AC Goianiense GO", "EC Vitória BA", "Corinthians", "Grêmio", "Fluminense RJ")
print("=-" * 50)
print(f"Lista de times do Brasileirão: {times}")
print("=-" * 50)
print(len(times))
print("=-" * 50)
print(f"Os 5 primeiros são {times[0:5]}")
print("=-" * 50)
print(times[16:])
print("=-" * 50)
print(f"Os 4 últimos são {times[-4:]}")
print("=-" * 50)
print(f"Times em ordem alfabética: {sorted(times)}")
print("=-" * 50)
print(f"O Corinthians está na {times.index("Corinthians")+1}ª posição")
