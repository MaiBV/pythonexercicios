'''import math
an = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print("O ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}".format(an, seno, cosseno, tangente))'''

from math import radians, sin, cos, tan
an = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print("O ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}".format(an, seno, cosseno, tangente))