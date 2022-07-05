while True:
    try:
        numero = int(input("Digite um numero de 0 a 10: "))
    except ValueError:
        print("Deve ser fornecido um número inteiro.")
    else:
        if 0 <= numero <= 10:
            print(f"O número informado é {numero}")
            break
        else:
            print("O número deve estar entre 0 e 10")


