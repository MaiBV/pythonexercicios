d = float(input('Digite uma distância em metros: '))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print("A medida de {:.0f}m corresponde a {:.0f}km, {:.0f}hm e {:.0f}dam".format(d, km, hm, dam))
print("A distância de {:.0f}m corresponde a {:.0f}dm, {:.0f}cm e {:.0f}mm".format(d, dm, cm, mm))
