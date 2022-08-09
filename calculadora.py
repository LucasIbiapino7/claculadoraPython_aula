"""
calculadora
"""


def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo numero: "))

print("Digite:\n1 - soma\n2 - subtração")
escolha = int(input())

if escolha == 1:

    print(soma(n1, n2))

elif escolha == 2:

    print(sub(n1, n2))

elif escolha == 3:

    print(multi(n1, n2))

elif escolha == 4:

    print(div(n1, n2))

else:
    
    print("valor inválido")

