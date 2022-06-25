saque = int(input("Digite um valor: "))

if saque < 10 or saque > 600:
    print("O valor mínimo e máximo para saque é de R$10 e R$600, respectivamente.")
else:
    notas_de_100 = notas_de_50 = notas_de_10 = notas_de_5 = notas_de_1 = 0
    notas_de_100, saque = divmod(saque, 100) # valor do saque // pelas notas
    notas_de_50, saque = divmod(saque, 50)
    notas_de_10, saque = divmod(saque, 10)
    notas_de_5, notas_de_1 = divmod(saque, 5)

    if notas_de_100 > 0:
        print(f'{notas_de_100} nota(s) de 100.')

    if notas_de_50 > 0:
        print(f'{notas_de_50} nota(s) de 50.')

    if notas_de_10 > 0:
        print(f'{notas_de_10} nota(s) de 10.')

    if notas_de_5 > 0:
        print(f'{notas_de_5} nota(s) de 5.')

    if notas_de_1 > 0:
        print(f'{notas_de_1} nota(s) de 1.')