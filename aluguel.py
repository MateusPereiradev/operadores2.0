km= float(input('Digite aqui quantos km você rodou com o carro:'))
dias= int(input('Digite aqui quantos dias você ficou com o carro:'))
valor_km= km*0.15
valor_dias= dias*60
print(f'Referente aos km rodados por você, o valor a pagar é: R${valor_km:.2f}!')
print(f'Referente aos dias que você ficou com o carro, o valor a pagar é : R${valor_dias:.2f}!')
print(f'O valor total será: R${valor_km + valor_dias:.2f}!')

'''
 escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
 dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
 R$0.15 por Km rodado.
 '''
