def triangulo_de_numeros_crescente(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha):
            print(coluna, end="   ")
        print(" ")

triangulo_de_numeros_crescente(1)
triangulo_de_numeros_crescente(2)
print("--------")
triangulo_de_numeros_crescente(3)
print("--------")
triangulo_de_numeros_crescente(4)