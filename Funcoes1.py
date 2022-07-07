def triangulo_de_numeros(n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end="   ")
        print(" ")

triangulo_de_numeros(1)
print("--------")
triangulo_de_numeros(2)
print("--------")
triangulo_de_numeros(3)
print("--------")
triangulo_de_numeros(4)