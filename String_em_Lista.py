frase = input("Digite uma frase: ").upper()


inverter_letras = "".join(reversed(frase))
inverter_palavras = " ".join(reversed(frase.split()))

print(f"Frase:{frase}")
print(f"Frase com as letras invertidas {inverter_letras}")
print(f"Frase com as palavras invertidas {inverter_palavras}")



