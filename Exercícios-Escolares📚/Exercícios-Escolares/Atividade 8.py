salario = float(input("Qual o seu salario: "))
sa = salario * 0.20
sa2 = salario * 0.15
sa3 = salario * 0.10
sa4 = salario * 0.05
sa1 =salario + sa

if salario <= 280:
	print(f"seu salario é{sa1}")
elif salario >= 280:
	print(f"Seu salario é  {sa2 + salario}")
elif salario >= 700:
	print(f"Seu salario é {sa3 + salario}")
elif salario >= 1500:
	print(f"Seu salario é {sa4 + salario}")

if salario == 1500:
	print("seu salario era {salario}, Agora está {salario + sa4}")