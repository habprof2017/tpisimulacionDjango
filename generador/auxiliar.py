import random


def generador(lote):
    minLote, maxLote = 0.333333, 0.397766

    if lote == "lote2":
        minLote, maxLote = 0.003519, 0.008310

    r = round(random.random(), 6)

    valor = round(round(maxLote - minLote, 6) * r + minLote, 6)
    # x = (b - a)*r + a
    print(type(minLote))
    print(type(maxLote))
    print(minLote)
    print(maxLote)
    return valor


print(generador("lote2"))
