# Cap05 - Lab 2 - Exercício calculadora simples
def calculadora(op,numero1,numero2):
    args = locals()
    for k in args:
        if not eh_numero(args[k]):
            return ">>> Atenção: um ou mais parâmetros fornecidos não é um número! <<<"

    switch={
        1: soma(numero1,numero2),
        2: subtracao(numero1,numero2),
        3: multiplicacao(numero1,numero2),
        4: divisao(numero1,numero2)
    }
    return switch.get(int(op),">>> Selecione uma opção válida. <<<")

def soma(numero1,numero2):
    return " {} + {} = {}".format(numero1, numero2, (numero1 + numero2))

def subtracao(numero1,numero2):
    return " {} - {} = {}".format(numero1, numero2, (numero1 - numero2))

def multiplicacao(numero1,numero2):
    return " {} * {} = {}".format(numero1, numero2, (numero1 * numero2))

def divisao(numero1,numero2):
    if numero2 == 0:
        return ">>> Não é possível a divisão de um número por zero! <<<"
    return " {} / {} = {}".format(numero1, numero2, (numero1 / numero2))

def converte_numero(numero):
    try:
        if numero.isdigit():
            return int(numero)
        else:
            return float(numero)
    except ValueError:
        return 'nan' 

def converte_opcao(numero):
    try:
        return int(numero)
    except ValueError:
        return 'nan'
    
def eh_numero(numero):
    if str(numero).lower() == str('nan'):
        return False
    return True

def main():
    print("\n***************************** Calculadora em Python ***************************** ")
    print("\n\n")
    print("> Selecione o número da operação desejada:")
    print("\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("\n")

    opcao = converte_opcao(input("Digita sua opção (1 / 2 / 3 / 4): "))
    print("\n")
    num1 = converte_numero(input("Forneça o primeiro número: "))
    print("\n")
    num2 = converte_numero(input("Forneça o segundo número: "))
    print("\n")
    
    print(calculadora(opcao,num1,num2))
    print("\n\n")
    print("\n***************************** FIM ***************************** ")

if __name__ == "__main__":
    main()