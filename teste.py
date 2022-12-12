
from diofantina import *
import random

entradas = [
    [1, 2, 2],
    [97, 43, 1],
    [123, -351, 2022],
    [-2, 1, 2],
    [1, -2, 2],
    [-2, -4, -8],
    [6, 4, 5]
]

# entradas = [[-2, -4, -8]]

def r():
    return int(random.random()*2000)-500

# for e in entradas:
for i in range(100):
    # a, b, c = e[0], e[1], e[2]
    a, b, c = r(), r(), r()
    
    erro = ""

    # resultado = resolveDiofantina(a, b, c, True)
    try:
        resultado = resolveDiofantina(a, b, c, False)
    except:
        erro = "de exceção"
        resultado = False

    eq = f"{a}x + {b}y = {c}"
    print(f"{eq :<20}", end=' ')

    if resultado is None:
        print(f"SS")
    elif resultado:
        print(f"OK")
    else:
        print(f"ERRO {erro}")

