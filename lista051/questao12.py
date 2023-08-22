'''
12)	Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem como maior, nem como menor, e nem na contagem da média.
'''

n = float(input("Digite um número (-1 encerra o programa): "))
maior = n
menor = n
contador = 0
acumulador = 0

while (n != -1):
    acumulador = acumulador + n
    contador = contador + 1

    if (maior < n):
        maior = n

    if (menor > n):
        menor = n
    n = float(input("Digite um número (-1 encerra o programa): "))

if (maior == -1):
    print("Você inseriu -1 na primeira resposta.\nPROGRAMA ENCERRADO")
else:
    print(f"O maior número inserido foi: {maior:.0f}, o menor foi: {menor:.0f} e a média dos números inseridos é: {acumulador / contador}.")
    print("FIM DO PROGRAMA")
