from math import sqrt


def primos_circulares(n):
    def eh_primo(num):
        if num == 1:
            return False

        limite = int(sqrt(num)) + 1
        for i in range(2, limite):
            if num % i == 0:
                return False

        return True

    def rotacoes(num):
        possiveis_rotacoes = []
        digitos = str(num)

        for _ in range(len(digitos)):
            # avancando os digitos em 1 unidade
            digitos = digitos[1:] + digitos[0]
            possiveis_rotacoes.append(int(digitos))

        return possiveis_rotacoes

    primos_circulares = []
    for i in range(2, n+1):
        if eh_primo(i):
            possiveis_rotacoes = rotacoes(i)
            eh_primo_circular = True
            for possibilidade in possiveis_rotacoes:
                if not eh_primo(possibilidade):
                    eh_primo_circular = False
                    break

            if eh_primo_circular:
                primos_circulares.append(i)

    return primos_circulares

# 123
# 1234
# 2341
# 3412
# 4123


print(primos_circulares(100))
