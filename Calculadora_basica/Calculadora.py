"""
Esse é um texte de variação de repetição
"""
operation_2 = 's'
while operation_2 == "s":
    go = input("Deseja fazer uma conta? [s]im ou [n]ão? ")
    if go == "s":
        print("Que operação você deseja fazer?")   
        operation = input(f" (1) Adição \n (2) Subtração \n (3) Multiplicação   \n (4) Divisão \n")
        if operation == '1':
            num_1 = input("Digite o primeiro numero: ")
            num_2 = input("Digite o segundo numero: ")
            if not num_1.isnumeric() and not num_2.isnumeric():
                print("Esses não são valores válidos para a operação. ")
            num_1 = float(num_1)
            num_2 = float(num_2)
            result = num_1 + num_2
            print(f"O resultado de {num_1} + {num_2} é {result}")
        elif operation == '2':
            num_1 = input("Digite o primeiro numero: ")
            num_2 = input("Digite o segundo numero: ")
            if not num_1.isnumeric() and not num_2.isnumeric():
                print("Esses não são valores válidos para a operação. ")
            num_1 = float(num_1)
            num_2 = float(num_2)
            result = num_1 - num_2 
            print(f"o resultado de {num_1} - {num_2} é {result}")
        elif operation == '3':
            num_1 = input("Digite o primeiro numero: ")
            num_2 = input("Digite o segundo numero: ")
            if not num_1.isnumeric() and not num_2.isnumeric():
                print("Esses não são valores válidos para a operação. ")
            num_1 = float(num_1)
            num_2 = float(num_2)
            result = num_1 * num_2 
            print(f'O resultado de {num_1} X {num_2} é {result}')
        elif operation == '4':
            num_1 = input("Digite o primeiro numero: ")
            num_2 = input("Digite o segundo numero: ")
            if not num_1.isnumeric() and not num_2.isnumeric():
                print("Esses não são valores válidos para a operação. ")
            num_1 = float(num_1)
            num_2 = float(num_2)
            result = num_1 / num_2
            print(f'O resultado de {num_1} / {num_2} é {result}')
        else:
            print("Essa não é uma operação válida.")
        operation_2 = input("Deseja fazer outra operação? [s]im ou [n]ão? ")
    else:
        operation_2 = False
print("Finalizando...")
    