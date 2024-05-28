l = float(input('largura da parede: '))
a = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {:.2f} X {:.2f} e sua área é de {}m²'.format(l, a, l * a), '.')
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format((l * a) / 2), '.')
