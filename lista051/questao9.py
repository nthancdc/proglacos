'''
9)	Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize um laço que efetue a variação de 2 em 2.
'''

cont = 0
acumulador = 0


while (cont <= 500):
    acumulador = acumulador + cont
    cont = cont + 2
print(f"A soma dos valores pares de 0 à 500 é: {acumulador}")

