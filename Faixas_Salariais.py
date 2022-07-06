salarios = [200, 252, 340, 415, 550, 680, 790, 880, 998, 997, 2000, 3000]
contagem_faixa_salarial = [0] * 9

for salario in salarios:
    indice = salario // 100 - 2
    indice_maximo = len(contagem_faixa_salarial) -1
    indice = min(indice, indice_maximo)
    contagem_faixa_salarial[indice] += 1
print(contagem_faixa_salarial)