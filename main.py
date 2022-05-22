a = [0]
while True:
    try:
        numero = int(input("Numero: "))
        numero2 = int(input("Numero 2: "))
        print('\n')
        if numero > a[-1] and numero2 == 2:
            a.append(numero)
        else:
            print("BBB")
        print(a)
    except ValueError:
         print("Algo deu errado")
