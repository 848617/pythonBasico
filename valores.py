resultado = 0

while True:

    melância = float(input(" digite o valor da melância "))
    arroz = float(input("digite o valor do arros "))
    bolacha = float(input("digite o valor da bolacha "))
    op = input(" informe a operação ")

    if op == '+':
        resultado = melância + arroz + bolacha
    elif op == '-':
        resultado = melância - arroz - bolacha
    elif op == '*':
        resultado = melância * arroz * bolacha
    elif op == '/':
        resultado = melância / arroz / bolacha
    else:
        print ("opção invalidade")



    print(f" o resultado é {resultado}")
    



