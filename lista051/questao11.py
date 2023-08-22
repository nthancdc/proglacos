'''
11)	Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um expoente qualquer (Variável e), ou seja, de be. (Sem usar Math.pow();)
'''

b = float(input("Me diga a base: "))
e = float(input("Me diga o expoente: "))

cont = 1
acumulador = 1

while (cont <= e):
    acumulador = acumulador * b
    cont = cont + 1
print(f"{b:.0f} elevado à {e:.0f} é: {acumulador:.0f}")

'''















'''


