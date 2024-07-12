from sympy import symbols, lambdify

# Definicja symbolu i równania
x = symbols('x')
rownanie = x**2 + 3*x - 15
rownanie_lambda = lambdify(x, rownanie, 'numpy')


def oblicz_dowolne_rownanie(f, argument):
    return f(argument)


def dekoracja(wzor):
    def dekorator(f):
        def wrapper(argument):
            print("=================")
            print(f"Równanie funkcji: {wzor}")
            print(f"Argument x: {argument}")
            wynik = f(argument)
            print(f"Wynik: {wynik}")
            print("=================")
        return wrapper
    return dekorator


def przykladowa_funkcja(argument):
    return oblicz_dowolne_rownanie(rownanie_lambda, argument)


@dekoracja(str(rownanie))
def przykladowa_funkcja_dekoracja(argument):
    return oblicz_dowolne_rownanie(rownanie_lambda, argument)


print(przykladowa_funkcja(5))
print()
przykladowa_funkcja_dekoracja(5)
