km_percorridos= float(input('Digite a quantidade de Km percorridos:'))
dias_alugados= int(input('Digite a quantidade de dias que o carro foi alugado:'))
preco_total= (km_percorridos * 0.15) + (dias_alugados * 60)
print(f'O preço total a pagar pelo aluguel do carro é de R${preco_total:.2f}!')

'''
 escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
 dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
 R$0.15 por Km rodado.
 '''
