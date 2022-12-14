"""
Integrantes

Pedro Lucas Santana         - 202017049
Marcelo A. dos Santos       - 160035481
Heitor Marques S. Barbosa   - 202016462

"""

import os

def clear():
    os.system("clear")

clear()

flipou = False

def mod(a, b):
    r = a % b
    if r<0: r= abs(b) + r
    return r

def ler_inteiro(msg, msg_erro="Erro! Digite um número inteiro: ", min=None):
    print(msg, end="")

    while True:
        numero = input("")

        try:
            numero = int(numero)

            if min is not None and numero < min:
                print(f"Erro! Digite um número ≥ {min}: ",end='')
                continue

            return numero
        except:
            print(msg_erro, end="")

class Eq:

    def __init__(self, e, d) -> None:
        self.esq = e
        self.dir = d
    
    def mult(self, valor):
        for k, v in self.esq.items():
            self.esq[k] *= valor
        for k, v in self.dir.items():
            self.dir[k] *= valor
        
    
    def mostrar(self):
        def mostraLado(lado):
            termos = []
            for k, v in lado.items():
                if v==1:
                    termos.append(f"{k}")
                elif v<0:
                    termos.append(f"{k}*({v})")
                else:
                    termos.append(f"{k}*{v}")

            print(" + ".join(termos), end='')
        
        mostraLado(self.esq)
        print(" = ",end='')
        mostraLado(self.dir)
        print("")


def substituir(eq1, eq2):
    # subs eq1 na eq2
    # deve ter 1 termo na eq1 isolado, e substituir nos termos iguas na eq2
    asubstituir = list(eq1.esq.keys())[0]

    # identificar termo
    acompanhaAsubs = eq2.dir.pop(asubstituir)

    for key, value in eq1.dir.items():
        if key in eq2.dir:
            eq2.dir[key] += value * acompanhaAsubs
        else:
            eq2.dir[key] = value * acompanhaAsubs

def calculaEquacoes(a, b, c):

    if b == 0 or abs(a) > abs(b):
        a, b = b, a

    equacoes = []

    while True:

        q = int(a / b)
        # r = mod(a, b)
        r = round((a/b - q) * b)

        if r<0:
            r += b
            q -= 1

        # print(f"og {a} = {b} * {q} + {r}")
        if r == 0:
            # print("")
            return equacoes

        # já salva com resto isolado: r = a + b *(-q)
        equacoes.append(Eq({r:1}, {a:1, b:-q}))

        a,b = b,r
    

def resolveDiofantina(a, b, c, printar=True):
    global flipou
    flipou = False

    if a<0 and b<0:
        flipou = True
        a, b, c = -a, -b, -c

    equacoes = calculaEquacoes(a, b, c)

    # for e in equacoes:
    #     e.mostrar()

    eqPrincipal = equacoes.pop(len(equacoes)-1)
    mdc = list(eqPrincipal.esq.keys())[0]

    if flipou: a, b, c = -a, -b, -c

    if printar: print(f"equação: {a}*x + {b}*y = {c}\n")

    if mod(c, mdc) != 0:
        if printar: print(f"essa equação não tem solução pois mdc({a},{b}) = {mdc}, e {mdc} não divide {c}")
        return None
    else:
        if printar: print(f"essa equação tem solução pois mdc({a},{b}) = {mdc}, e {mdc} | {c}\n")
    
    if flipou: a, b, c = -a, -b, -c
    
    # print("substituindo")
    for i in range(1, len(equacoes)+1):
        eq = equacoes[len(equacoes) - i]
        substituir(eq, eqPrincipal)
    
    #     eqPrincipal.mostrar()
    # print("")
    
    eqPrincipal.mult(int(c/mdc))

    x = eqPrincipal.dir[a]
    y = eqPrincipal.dir[b]

    if flipou: a, b, c = -a, -b, -c

    if a*x + b*y != c:
        if printar: print(f"erro, a sol. x = {x}, y = {y} não resolve a equação")
        return False

    if printar:
        
        print(f"solução particular: x0 = {x}, y0 = {y}\n")

        sinal = '+' if int(a/mdc) < 0 else '-'
        print(f"equação da solução geral")
        print(f"x = {x} + {int(b/mdc)} * t")
        print(f"y = {y} {sinal} {abs(int(a/mdc))} * t")

        print("\ncom base na sol. geral, aqui uns exemplos")
        for t in range(1, 4):
            xt = x + int(b/mdc) * t
            yt = y - int(a/mdc) * t
            print(f"t={t}:  x = {xt}, y = {yt} -> {a}({xt}) + ({b})({yt}) = {a*xt} + ({b*yt}) = {a*xt + b*yt}")

    return True
    

if __name__ == '__main__':
    print("formato da equação: ax + by = c\n")
    a = ler_inteiro("digite o valor de a: ")
    b = ler_inteiro("digite o valor de b: ")

    if a==0 and b==0:
        print(f"a e b não podem ser nulos ao mesmo tempo")
    else:

        c = ler_inteiro("digite o valor de c: ")

        clear()

        resolveDiofantina(a, b, c)

