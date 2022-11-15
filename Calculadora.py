# calculadora simples

# Esta função adiciona dois números
import math


def add(x, y):
    return x + y


# Esta função subtrai dois números
def subtract(x, y):
    return x - y


# Esta função multiplica dois números
def multiply(x, y):
    return x * y


# Esta função divide dois números, retorna None se numerador for zero
def divide(x, y):
    if y == 0:
        return None
    return x / y


# Esta função faz a potencialização de dois números
def potentiation(x, y):
    return x ** y


# Esta função faz a percentagem de um número
def percentage(x):
    return x / 100


# Esta função faz a raiz quadrada de um número
def squareroot(x):
    if x >= 0:
        return math.sqrt(x)
    return None


def calc():
    while True:
        print("Selecione a operação.")
        print("1.Adicionar                   5.Potenciação")
        print("2.Subtrair                    6.Percentagem")
        print("3.Multiplicação               7.Raiz Quadrada")
        print("4.Divisão                     8.Operação Complexa")
        print("Sair")
        print("")
        # Obter a escolha do utilizador
        choice = input("Escola entre (1/2/3/4/5/6/7/8): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                number1 = float(input("Coloque o primeiro número: "))
            except:
                print("Deve inserir um número ")
                print()
                calc()

            try:
                number2 = float(input("Coloque o segundo número: "))
            except:
                print("Deve inserir um número ")
                print()
                calc()

            if choice == '1':
                print(number1, "+", number2, "=", add(number1, number2))

            elif choice == '2':
                print(number1, "-", number2, "=", subtract(number1, number2))

            elif choice == '3':
                print(number1, "*", number2, "=", multiply(number1, number2))

            elif choice == '4':
                if divide(number1, number2) is not None:
                    print(number1, "/", number2, "=", divide(number1, number2))
                print("Não é possível dividir por zero")

            elif choice == '5':
                print(number1, "^", number2, "=", potentiation(number1, number2))

        elif choice == '7' or choice == '6':
            number1 = float(input("Coloque o número que pretende: "))

            try:
                number1 = float(input("Coloque o primeiro número: "))
            except:
                print("Deve inserir um número ")
                print()
                calc()

            if choice == '6':
                print(number1, "%" "=", percentage(number1))

            elif choice == '7':
                if squareroot(number1) is not None:
                    print(number1, "√", " =", squareroot(number1))
                print('Nao pode fazer a raiz quadrada de um número inferior a 0')

        elif choice == '8':
            try:
                exp = input("Coloque a expressão:")
                result = eval(exp)
                print('O resultado da expressão :', exp, 'é', result)
            except:
                print('Expressão invalida')

        elif choice == 'sair' or choice == 'Sair':
            break

        else:
            print("input invalido")

        # verifica se o utilizador que fazer mais contas
        next_calculation = input("Quer continuar? (sim/não): ")
        if next_calculation == "sim" or next_calculation == "s" or next_calculation == "yes":
            print()
        else:
            print("input invalido")
            break


if __name__ == '__main__':
    calc()
