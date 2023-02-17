Resultado = 0 

while True:
    n1 = float(input(" digite ovalor 1 "))
    n2 = float(input(" digite o valor 2 "))
    op = input("informe a operação: ")
    
    if op == '+':
        Resultado = n1 + n2 
    elif op == '-':
        Resultado = n1 - n2
    elif op == '*':
        Resultado = n1 * n2
    elif op == '/': n1 / n2
    else:
        print("opção invalida")
    print(f" o Resultado é {Resultado}" )