produto= float(input("Digite o valor do produto:R$"))
produto_desconto= produto*5/100
produto_prazo= produto*8/100
print(f"Referente ao valor do produto R${produto} o valor com 5% de desconto é R${produto-produto_desconto:.2f}")
print(f"Referente ao valor do produto R${produto} o valor com 8% de juros é R${produto+produto_prazo:.2f}")


# mostre o valor de um produto com 5% de desconto e outro valor a prazo com 8% de acréscimo em cima do valor do produto.
