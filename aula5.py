# armazena um número pequeno
maior_numero = -99999999

#entra com o primeiro número
number = int(input("Entre com um número ou digite -1 para parar: "))

#Se o número não for igual a -1 continua
while number != -1:
    if number > maior_numero:
        maior_numero = number
    number = int(input("Entre com um número ou digite -1 para parar: "))

#Imprime o maior número
print("O maior número è o: ", maior_numero)