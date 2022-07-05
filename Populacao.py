populacao_a = 80_000
populacao_b = 200_000
taxa_de_crescimento_de_a = 1.03
taxa_de_crescimento_de_b = 1.015
anos = 0

while populacao_a < populacao_b:
    populacao_a = int(populacao_a * taxa_de_crescimento_de_a)
    populacao_b = int(populacao_b * taxa_de_crescimento_de_b)
    anos +=1

print(f"#### Populações no ano {anos}")
print(f"População de A: {populacao_a}")
print(f"População de B: {populacao_b}")


