def converterDecimalParaBinario(decimal, comprimento_decimal):
    resultado = ""

    while comprimento_decimal:
        decimal = str(decimal * 2)
        
        primeiro_digito = decimal[0:1]

        decimal = float(decimal)
        
        if primeiro_digito == "1":
            decimal = decimal - 1

        resultado += primeiro_digito

        comprimento_decimal -= 1
    return resultado


numero = input("Digite um número decimal: ")    # supondo número 263.3
tipo = 32   # 32 bits

# Passo 1: Tranformar as partes inteira e decimal em binário
inteiro = numero.split(".")[0]  # 263
decimal = float(numero) - int(inteiro)  # 0.3

print("Parte inteira:", inteiro) 
print("Parte decimal:", decimal)

inteiro_binario = bin(int(inteiro)).lstrip("0b")    # 100000111
comprimento_sinal = 1
comprimento_expoente = len(inteiro_binario) - comprimento_sinal # 8
comprimento_decimal = 32 - (comprimento_sinal + comprimento_expoente)   # 23
decimal_binario = converterDecimalParaBinario(decimal, comprimento_decimal) # 01001100110011001100110

print("Parte inteira em binário:", inteiro_binario)
print("Parte decimal em binário:", decimal_binario)

# To Do List:
# - Criar uma versão para 64 bits
# - Perguntar a Aragão porque a parte decimal adquire uns números nas casas mais baixas