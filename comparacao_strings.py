s1 = input("Digite uma string: ")
s2 = input("Digite uma string: ")

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'{s1}: {tamanho1} caracteres ')
print(f'{s2}: {tamanho2} caracteres ')

comparacao_tamanho = "diferentes"
comparacao_conteudo = "diferente"

if s1 == s2:
    comparacao_tamanho = "iguais"
    comparacao_conteudo = "igual"
elif tamanho1 == tamanho2:
    comparacao_tamanho = "iguais"

print(f'As duas strings são de tamanhos {comparacao_tamanho}.')
print(f'As duas strings são de conteúdo {comparacao_conteudo}.')