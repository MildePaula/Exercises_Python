# Fazer um programa que leia um número determinado de valores;
# A entrada é encerrada quando o input for -1;
# Mostre a quantidade de valores lidos;
# Exiba os valores na ordem que foram informados;
# Exiba os valores na ordem inversa;
# Calcular os valores acima da média;
# Calcular os valores abaixo de 7;
# Encerrar o programa com uma mensagem.

notas = []

while True:
    valor_entrada = input("Digite a nota: ")
    if valor_entrada == "-1":
        break
    notas.append(float(valor_entrada))

tamanho = len(notas)
print(f"Foram lidas {tamanho} notas.")
print(" ".join([str(nota) for nota in notas])) # list comprehension
notas.reverse()

for nota in notas:
    print(nota)

soma = sum(notas)
print(f"A soma das notas é {soma}.")

media = soma / tamanho
print(f"A media das notas é {media}.")

print("Notas acima da média: ")
print(" ".join([str(nota) for nota in notas if nota > media]))

print("Notas abaixo de 7: ")
print("".join([str(nota) for nota in notas if nota < 7]))

print("Programa encerrado")