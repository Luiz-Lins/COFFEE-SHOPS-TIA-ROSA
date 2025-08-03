produtos = {}

while True:
    produto = input("digite o nome do produto (ou 'sair' para finalizar):")
    if produto.lower() == 'sair':
        break
    try:
        categoria = input(str(f"Digite a categoria do produto {produto}: "))
        produtos[produto] = categoria
        print(f"Produto '{produto}' cadastrado com sucesso!")
    except ValueError:
        print("categoria errada, por favor insira algo como (bebida, salgados, porções ou drinks.")

print("\n--- Produtos Cadastrados ---")
for nome, categoria in produtos.items():
     print(f"Produto: {nome} | Categoria: {categoria}")