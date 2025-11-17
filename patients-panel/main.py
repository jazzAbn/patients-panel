import sys

# Lista global para armazenar os dados dos pacientes
# Inicializamos a lista aqui para que ela esteja disponível em todas as funções
pacientes = []

# --- FUNÇÕES DO MENU ---

def exibir_menu():
    """Exibe as opções do menu para o usuário."""
    print("\n" + "="*30)
    print("🏥 Menu Gerenciador de Pacientes")
    print("="*30)
    print("1. Adicionar Novo Paciente")
    print("2. Exibir Todos os Pacientes")
    print("3. Análise de Dados (Média/Min/Max)")
    print("4. Buscar Paciente por Nome")
    print("5. Sair")
    print("-" * 30)

def adicionar_paciente():
    """
    Solicita os dados do paciente e os adiciona à lista global 'pacientes'.
    """
    print("\n--- Adicionar Paciente ---")
    while True:
        try:
            nome = input("Nome do paciente: ").strip().lower()
            if not nome:
                print("O nome não pode ser vazio.")
                continue

            idade = int(input("Idade do paciente: "))
            if idade <= 0:
                print("A idade deve ser um número positivo.")
                continue

            telefone = input("Telefone do paciente: ").strip()

            pacientes.append({'nome': nome, 'idade': idade, 'telefone': telefone})
            print(f"✅ Paciente '{nome.capitalize()}' cadastrado com sucesso!")
            break
        except ValueError:
            print("❌ Erro: Por favor, insira um valor numérico válido para a idade.")

def exibir_pacientes():
    """
    Exibe a lista completa de pacientes, ordenados por idade.
    """
    if not pacientes:
        print("\nLista vazia. Cadastre um paciente primeiro (Opção 1).")
        return
        
    ordenados = sorted(pacientes, key=lambda x: x['idade'])
    
    print(f"\n--- Pacientes Cadastrados ({len(pacientes)} total) ---")
    for p in ordenados:
        
        print(f"Nome: {p['nome'].capitalize()} | Idade: {p['idade']} | Tel: {p['telefone']}")

def analise_dados():
    """
    Calcula e exibe a média de idade, o paciente mais novo e o mais velho.
    """
    if not pacientes:
        print("\nNão há dados para análise. Cadastre um paciente primeiro (Opção 1).")
        return

    print("\n--- Análise Estatística ---")

    
    soma_idades = sum(p['idade'] for p in pacientes)
    media_idade = soma_idades / len(pacientes)
    print(f"Total de pacientes cadastrados: {len(pacientes)}")
    print(f"Média das idades: {media_idade:.2f} anos")

    
    mais_novo = min(pacientes, key=lambda x: x['idade'])
    mais_velho = max(pacientes, key=lambda x: x['idade'])
    
    print(f"Paciente mais novo: {mais_novo['nome'].capitalize()} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome'].capitalize()} ({mais_velho['idade']} anos)")


def buscar_paciente():
    """
    Busca um paciente pelo nome e exibe seus detalhes.
    """
    if not pacientes:
        print("\nNão há pacientes para buscar. Cadastre um paciente primeiro (Opção 1).")
        return

    print("\n--- Buscar Paciente ---")
    buscar = input("Digite o nome do paciente que deseja localizar: ").strip().lower()
    
    
    encontrados = [p for p in pacientes if p['nome'] == buscar]

    if encontrados:
        print(f"\nPaciente(s) encontrado(s): {len(encontrados)}")
        for p in encontrados:
            print(f"\nNome: {p['nome'].capitalize()}\nIdade: {p['idade']}\nTelefone: {p['telefone']}")
    else:
        print(f"\n❌ Paciente com o nome '{buscar.capitalize()}' não encontrado.")




def main():
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_paciente()
        elif opcao == "2":
            exibir_pacientes()
        elif opcao == "3":
            analise_dados()
        elif opcao == "4":
            buscar_paciente()
        elif opcao == "5":
            print("\nObrigado por usar o Gerenciador de Pacientes. Encerrando o sistema...")
            sys.exit() # Encerra o programa
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 5.")


if __name__ == "__main__":
    main()