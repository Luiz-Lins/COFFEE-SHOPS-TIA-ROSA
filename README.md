# COFFEE-SHOPS-TIA-ROSA
# Sistema de Gerenciamento de Pedidos para Cafeteria

Este é um sistema simples em Python para gerenciar o catálogo de produtos e os pedidos de uma cafeteria. Ele permite 
o cadastro de produtos com categoria e preço, o registro de pedidos de clientes e, por fim, a emissão de um resumo 
detalhado de todos os pedidos com seus respectivos totais.

O projeto foi desenvolvido com uma arquitetura orientada a objetos, utilizando **classes** e **funções** para manter 
o código organizado, modular e fácil de entender.

---

## Funcionalidades

- **Cadastro de Produtos**: Adicione produtos ao catálogo com nome, categoria e preço.
- **Gerenciamento de Pedidos**: Registre pedidos para diferentes clientes. O sistema exibe os produtos disponíveis com um seletor numérico para facilitar a escolha.
- **Cálculo de Total**: O sistema calcula automaticamente o valor total de cada pedido.
- **Resumo de Pedidos**: Ao final, é gerado um resumo completo de todos os pedidos registrados, mostrando os itens, suas categorias e o valor total por cliente.

---

## Como Usar

Para usar o sistema, basta executar o script Python. O programa irá guiar você através de três etapas principais:

1.  **Cadastro de Produtos**:
    - O sistema pedirá que você insira o nome, a categoria e o preço de cada produto.
    - Digite `sair` para finalizar o cadastro e passar para a próxima etapa.

2.  **Gerenciamento de Pedidos**:
    - O sistema pedirá o nome do cliente.
    - Em seguida, exibirá a lista de produtos cadastrados com um número de identificação.
    - Você pode adicionar um produto ao pedido digitando o número correspondente.
    - Digite `0` para finalizar o pedido do cliente e passar para o próximo.

3.  **Resumo**:
    - Após finalizar todos os pedidos, o sistema exibirá um resumo completo, mostrando cada cliente, os itens que ele pediu e o total a pagar.

### Requisitos

- Python 3.x

### Execução

Para rodar o programa, salve o código em um arquivo `cafeteria_sistema.py` e execute o seguinte comando no terminal:

```bash
python cafeteria_sistema.py