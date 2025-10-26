
import uuid # Biblioteca importada para geração de id único

# Guarda estoque principal, sendo chave = id e valor = dicionário com informações do produto.
estoque = {} 

# Cadastro, remoção e edição

def cadastra_produtos(id_produto, nome, categoria, quantidade, preco):

    produtos = {
    "id": id_produto,
    "nome": nome,
    "categoria": categoria,
    "quantidade": quantidade,
    "preco": preco
    }
    estoque[id_produto]= produtos
    
def remove_produto(deleta_produto):
    
    if deleta_produto in estoque:
        del(estoque[deleta_produto])
        return f"\nProduto {deleta_produto} removido com sucesso!"
    else:
        return "\nProduto não encontrado."
    
def edita_produtos(edita_produto):
    if edita_produto in estoque:
        produto = estoque[edita_produto]
        print(f"\nProduto com id {edita_produto} sendo editado.")

        produto["nome"] = input("\nNovo nome: ") 
        produto["categoria"] = input("Nova categoria: ")
        produto["quantidade"] = int(input("Nova quantidade: "))
        produto["preco"] = float(input("Novo valor: R$ "))
        
        return f"\nProduto {edita_produto}: {produto["nome"]} editado com sucesso!"
    else:
        return f"\nProduto com id {edita_produto} não encontrado."

# Controle de estoque (regista entradas e saídas)

def registra_movimentacao(id_produto):

    if id_produto in estoque:
        produto = estoque[id_produto]
        print(f"\nProduto: {produto["nome"].upper()} - Quantidade atual: {produto["quantidade"]}.")

        tipo_movimentacao = input("\nDigite o tipo de movimentação [E/S]: ").strip().upper()
        quantidade = int(input("Quantidade entrada/saída: "))

        if tipo_movimentacao == "E":
            produto["quantidade"] += quantidade
            print(f"\nEntrada registrada com sucesso. Nova quantidade: {produto["quantidade"]}.")
        elif tipo_movimentacao == "S":
            if produto["quantidade"] >=5:
                produto["quantidade"] -= quantidade
                print(f"\nSaída registrada com sucesso. Nova quantidade: {produto["quantidade"]}.")
                if produto["quantidade"] <= 10: 
                    print("ALERTA: produto com baixa quantidade em estoque.")
            else: 
                print(f"\nNão foi possível completar a ação: quantidade de estoque abaixo do mínimo permitodo ({produto["quantidade"]}).")
        else:
            print("\nTipo de movimentação inválida, tente novamente!")
    else:
        print(f"\nProduto com ID {id_produto} não encontrado.")

# Consulta de produtos

def consulta_produtos(escolha):
    
    if escolha == "1":

        id_produto = input("\nDigite o ID do produto: ").strip().lower()
        
        produto = estoque[id_produto]
        
        if id_produto in estoque:
            exibir_produto(produto)
        else:
            print(f"Produto com ID {id_produto} não encontrado.")

    elif escolha == "2":
        nome_produto = input("Nome do produto: ").strip().lower()
        produto_encontrado = [prod for prod in estoque.values() if prod["nome"].lower() == nome_produto]
        if produto_encontrado:
            exibir_lista(produto_encontrado)
        else:
            print(f"Nenhum produto encontrado!")

    elif escolha == "3":
        categoria = input("Categoriado produto: ").strip().lower()
        produto_encontrado = [prod for prod in estoque.values() if prod["categoria"].lower() == categoria]
        if produto_encontrado:
            exibir_lista(produto_encontrado)

        else: 
            print(f"Nenhum produto encontrado!")
    else:
        print("Opção inválida! Tente novamente.")

def exibir_produto(produto):
    print("-" * 25)
    print(f"\nID: {produto["id"]}")
    print(f"Nome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Quantidade: {produto['quantidade']}")
    print(f"Preço: R${produto['preco']:.2f}")
    print("-" * 25)

def exibir_lista(lista):
    if not lista:
        print("\nNenhum produto encontrado.")
        return
    for produto in lista:
        exibir_produto(produto)

## Funções Relatórios 

def relatorios(tipo_relatorio):
    if tipo_relatorio == "1":
        print(f"\n{'Relatório de produtos':-^40}")
        for produto in estoque.values():
            exibir_produto(produto)

    elif tipo_relatorio == "2":
        print(f"{'\nRelatório de baixo estoque':-^40}")
        minimo = 5
        baixo = [prod for prod in estoque.values() if prod["quantidade"] < minimo]
        exibir_lista(baixo)
    
    else:
        print("Opção inválida! Tente novamente.")

# Menu
def menu():
    while True:
        print("\nGERENCIADOR DE ESTOQUE MERCADO COMER BEM")
        print("""
        1. Cadastrar produtos
        2. Remover produtos
        3. Editar produtos
        4. Controle de estoque (Entrada/Saída)
        5. Consulta de produtos
        6. Relatórios
        7. Encerrar sistema
        """)

        opcao = input("Digite a opção desejada (1,2,3,4,5,6,7): ").strip()

        if opcao == "1":
            print("Para cadastrar um novo produto digite: ")
            id_produto = str(uuid.uuid4())[:8]
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Valor: R$ "))
            cadastro = cadastra_produtos(id_produto, nome, categoria, quantidade, preco)
            print(f"\nProduto {nome} cadastrado com código {id_produto}.")
    
        elif opcao == "2":
            deleta_produto = input("Digite o ID do produto que deseja remover: ").strip().lower()
            resultado_remove_produto = remove_produto(deleta_produto)
            print(resultado_remove_produto)

        elif opcao == "3":
            print(f"\n{'ESTOQUE ATUAL':=^30}")
            for chave, valor in estoque.items():
                print(f"\nid: {chave}")
                print(f"Nome: {valor["nome"]}")
                print(f"Categoria: {valor["categoria"]}")
                print(f"Quantidade: {valor["quantidade"]}")
                print(f"Preço: {valor["preco"]}")
                print("="*20)
            edita_produto = input("Digite o ID do produto que deseja editar: ").strip().lower()
            print(edita_produtos(edita_produto))

        elif opcao == "4":
            print(f"\n{'Controle de estoque':=^20}")
            for chave, valor in estoque.items():
                print(f"\nid: {chave}")
                print(f"Nome: {valor["nome"].title()}")
                print(f"{'='*20}")
            id_produto = input("Digite o ID do produto: ").strip().lower()
            registra_movimentacao(id_produto)

        elif opcao == "5":
            print(f"\n{'Consultar produtos':-^10}")
            print("""
1. Consulta por ID
2. Consulta por nome
3. Consulta por Categoria
""")
            
            escolha = input("Digite qual o tipo de consulta deseja realizar (1,2,3): ")
            consulta_produtos(escolha)

        elif opcao == "6":
            print(f"\n{'Relatórios':-^20}")
            print("\nOpções de relatórios")
            print("""
1. Relatório de produtos
2. Relatório de produtos com baixo estoque
""")
            tipo_relatorio = input("Qual o tipo de relatório deseja gerar (1,2)? ").strip()
            relatorios(tipo_relatorio)

        elif opcao == "7":
            print("Encerrando programa...")
            break
    
        else:
            print("Opção inválida! Tente novamente.")
menu()

