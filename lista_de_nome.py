def menu():
    print("Menu:")
    print("1 - Cadastrar Pessoa")
    print("2 - Listar Pessoas")
    print("3 - Excluir Pessoa")
    print("0 - Sair")

def cadastrar_pessoa(pessoas):
    nome = input("Digite o nome da pessoa: ")
    idade = input("Digite a idade da pessoa: ")
    pessoas.append({"nome": nome, "idade": idade})
    print(f"Pessoa {nome} cadastrada com sucesso!")

def listar_pessoas(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
    else:
        print("\nLista de Pessoas:")
        for i, pessoa in enumerate(pessoas):
            print(f"{i + 1}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")

def excluir_pessoa(pessoas):
    listar_pessoas(pessoas)
    if pessoas:
        try:
            indice = int(input("Digite o número da pessoa que deseja excluir: ")) - 1
            if 0 <= indice < len(pessoas):
                pessoa_removida = pessoas.pop(indice)
                print(f"Pessoa {pessoa_removida['nome']} removida com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def main():
    pessoas = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_pessoa(pessoas)
        elif opcao == "2":
            listar_pessoas(pessoas)
        elif opcao == "3":
            excluir_pessoa(pessoas)
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()