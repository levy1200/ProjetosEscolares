s = float(input("Digite sua nota: "))
s1 = float(input("Digite outra nota:"))
s2 = s + s1
s3 = s2 / 2

if s3 >= 7:
	print("Aprovado")
elif s3 <= 7:
	print("Reprovado")
elif s3 == 10:
	print("Aprovado com distinção")
