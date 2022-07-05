maximo = float(input("Digite um número: "))
for _ in range(4):
    maximo = max(maximo, float(input("Digite um número: ")))
    print(f"O número máximo é: {maximo}")