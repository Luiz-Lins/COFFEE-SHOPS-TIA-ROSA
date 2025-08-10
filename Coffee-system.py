class Produto:
    # Classe de produtos com nome, categoria e preço.

    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco


class Pedido:
    # Classe de pedidos.

    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []  # A lista de itens do pedido será uma lista de objetos Produto

    def adicionar_item(self, produto):
        # Função para adicionar um produto à lista de itens do pedido.
        self.itens.append(produto)

    def calcular_total(self):
        # Calcula e retorna o valor total do pedido.
        total = sum(item.preco for item in self.itens)
        return total


def cadastrar_produtos(produtos_cadastrados):
    # Função para gerenciar o cadastro de novos produtos.
    print("\n--- Cadastro de Produtos -> << Agora vamos adicionar produtos ao catalogo >> --- ")
    while True:
        nome = input("Digite o produto a ser cadastrado (ou 'sair' para finalizar o cadastro de produtos): ")
        if nome.lower() == 'sair':
            break

        categoria = input(f"Digite a categoria do produto '{nome}': ")

        try:
            preco = float(input(f"Digite o preço do produto '{nome}': "))
            # Cria um objeto Produto e o adiciona ao dicionário
            produtos_cadastrados[nome] = Produto(nome, categoria, preco)
            print(f"Produto '{nome}' cadastrado com sucesso!")
        except ValueError:
            print("Preço inválido. Por favor, insira um número. Tente novamente.")
            continue


def exibir_produtos_cadastrados(produtos_cadastrados):
    # Função para exibir os produtos cadastrados com um índice de seleção.
    print("\n--- Produtos Disponíveis ---")
    if not produtos_cadastrados:
        print("Nenhum produto cadastrado.")
        return []

    # Cria uma lista de tuplas (índice, objeto_produto)
    lista_de_produtos = list(produtos_cadastrados.values())
    for i, produto in enumerate(lista_de_produtos):
        print(f"[{i + 1}] {produto.nome} (Categoria: {produto.categoria}) - R${produto.preco:.2f}")

    return lista_de_produtos


def gerenciar_pedidos(produtos_cadastrados):
    # Função para gerenciar o registro de novos pedidos.
    pedidos_registrados = []
    print("\n--- Agora vamos adicionar pedidos --- \n --- Gerenciamento de Pedidos ---")

    while True:
        cliente = input("Digite o nome do cliente (ou 'sair' para finalizar os pedidos): ")
        if cliente.lower() == 'sair':
            break

        # Exibe os produtos para o usuário escolher
        lista_de_produtos = exibir_produtos_cadastrados(produtos_cadastrados)
        if not lista_de_produtos:
            continue

        pedido_atual = Pedido(cliente)  # Cria um novo objeto Pedido para o cliente

        while True:
            try:
                # O usuário do sistema digita o número um número que diz respeito a um produto da lista
                selecao = input(f"Digite o número do produto para {cliente} (ou '0' para finalizar o pedido): ")

                if selecao == '0':
                    break

                indice = int(selecao) - 1

                if 0 <= indice < len(lista_de_produtos):
                    produto_escolhido = lista_de_produtos[indice]
                    pedido_atual.adicionar_item(produto_escolhido)
                    print(f"'{produto_escolhido.nome}' adicionado ao pedido de {cliente}.")
                else:
                    print("Erro: Número inválido. Por favor, escolha um número da lista.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        pedidos_registrados.append(pedido_atual)
        print(f"\nPedido de {cliente} finalizado com {len(pedido_atual.itens)} itens.")

    return pedidos_registrados


def imprimir_resumo(pedidos_registrados):
    """Função para imprimir um resumo de todos os pedidos."""
    print("\n--- Resumo de Todos os Pedidos ---")
    if not pedidos_registrados:
        print("Nenhum pedido foi registrado.")
        return

    for pedido in pedidos_registrados:
        print(f"\nCliente: {pedido.cliente}")
        if pedido.itens:
            for item in pedido.itens:
                print(f" - {item.nome} (Categoria: {item.categoria}) - R${item.preco:.2f}")

            total = pedido.calcular_total()
            print(f"Total do Pedido: R${total:.2f}")
        else:
            print(" - Nenhum item neste pedido.")


# --- Execução Principal do Sistema da cafeteria ---

# Dicionário para armazenar os objetos Produto, usando o nome como chave
produtos = {}
# Lista para armazenar os objetos Pedido
pedidos = []

cadastrar_produtos(produtos)
if produtos:
    pedidos = gerenciar_pedidos(produtos)
    imprimir_resumo(pedidos)
else:
    print("Nenhum produto cadastrado. O gerenciamento de pedidos não pode ser iniciado.")