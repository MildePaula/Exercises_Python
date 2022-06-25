# Split the input into hundreds, tens and units
numero = int(input('Digite um número até 1000: '))
centenas_str = dezenas_str = unidades_str = ''

                                                #centenas_int = numero // 100 => A divisão está completa
centenas_int, numero = divmod(numero, 100)      # divmod é uma função. Através dela, pode-se obter tanto o resultado da divisão inteira quanto o resto:
                                                # o input (numero) é dividido por 100 para a centena ser encontrada e ser atrubuído à variavel(centenas_int)
                                                # o resto por sua vez é atribuído à variável numero.
partes_numericas = 0
if centenas_int == 1:
    centenas_str ='1 centena'
    partes_numericas += 1
elif centenas_int > 1:
    centenas_str = (f'{centenas_int} centenas')
    partes_numericas += 1

dezenas_int, numero = divmod(numero, 10) # calcular a dezena
if dezenas_int == 1:
    dezenas_str ='1 dezena'
    partes_numericas += 1
elif dezenas_int > 1:
    dezenas_str = (f'{dezenas_int} dezenas')
    partes_numericas += 1

if numero == 1:                                # Não é necessário usar o divmod porque o resto já está atribuído à variável numero
    unidades_str = '1 unidade'
    partes_numericas += 1
elif numero > 1:
    unidades_str = (f'{numero} unidades')
    partes_numericas += 1

if partes_numericas == 0:
    print('Este número não possui centenas, dezenas ou unidades.')
elif partes_numericas == 1:
    print(centenas_str + dezenas_str + unidades_str)
elif partes_numericas == 3:
    print(f'{centenas_str}, {dezenas_str} e {unidades_str}')
elif partes_numericas == 2:
    if centenas_str != '':
        segunda_parte = dezenas_str + unidades_str
        print(f'{centenas_str} e {segunda_parte}')
