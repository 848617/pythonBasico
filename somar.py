resultado = 0

while True:
	n1 = float(input("Digite valor 1: "))
	n2 = float(input("Digite valor 2: "))
	op = input("Informe a operação: ")

	if op == '+':
		resultado = n1 + n2
	elif op == '-':
		resultado = n1 - n2
	elif op == '*':
		resultado = n1 * n2
	elif op == '/':
		resultado = n1 / n2
	else:
		print("opção invalidade")
	
	print(f" O resultado é {resultado}")