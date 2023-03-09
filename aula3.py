numero_secreto = 42
tentativa = 1

while tentativa <= 3:
    palpite = int(input("Adivinhe o número secrero: "))
    if palpite == numero_secreto:
        print("Parábens, você acertou!")
        break
    
    else:
        if palpite > numero_secreto:
         print("o número secreto é menor do que", palpite)
        else:
         print("O número é maior do que", palpite)
    
        tentativa += 1

if tentativa > 3:
    print("Suas tentativas acabaram. O número secreto era", numero_secreto)