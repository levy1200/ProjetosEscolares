num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = int(input("Digite o 3 numero: "))

if num1 >= num2 and num1 >= num3:
	print(f"o {num1} é o maior dentre eles")
elif num2 >= num1 and num2 >= num3:
	print(f"o {num2} é o maior dentre eles")
elif num3 >= num1 and num3 >= num2:
	print(f"o {num3} é o maior dentre eles")

if num1 <= num2 and num1 <= num3:
	print(f"o {num1} é o menor dentre eles")
elif num2 <= num1 and num2 <= num3:
	print(f"o {num2} é o menor dentre eles")
elif num3 <= num1 and num3 <= num2:
	print(f"o {num3} é o menor dentre eles")
