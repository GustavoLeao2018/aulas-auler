"""
Faça um Programa que leia 2 números:
e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
numero1 = input("Digite o 1º número:")
numero2 = input("Digite o 2º número:")

texto = """Menu:
1 - Par ou Ímpar
2 - Positivo ou negativo
3 - Inteiro ou decimal
Escolha:
"""
opcao = int(input(texto))

if opcao == 1:
    if (int(numero1) % 2) == 0:
        print(f"O número: {numero1} É par.")
    else:
        print(f"O número: {numero1} É ímpar.")

elif opcao == 2:
    if int(numero1) < 0:
        print(f"O número: {numero1} É negativo.")
    else:
        print(f"O número: {numero1} É positivo.")

elif opcao == 3:
    if numero1.isdigit() is True:
        print(f"O número: {numero1} É inteiro.")
    else:
        print(f"O número: {numero1} É decimal.")

"""
TODO:
    1 - Completar o código para o número 2, dentro dos if's. 
    2 - Acrescentar NO FINAL um ELSE com um loop, pedindo ao usuário que digite novamente um número válido (obs.: número <= 3).
"""