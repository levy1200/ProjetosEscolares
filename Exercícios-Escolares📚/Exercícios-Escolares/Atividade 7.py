s = str(input("Em que Turno Você Estuda?(M, V ou N) ")).upper()
turno = s

if turno == "M":
	print("Bom Dia!")
elif turno == "V":
	print("Boa Tarde!")
elif turno == "N":
	print("Boa Noite!")
else:
	print("Valor Invalido!")