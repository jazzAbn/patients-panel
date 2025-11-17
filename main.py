import sys

pacientes = []

def exibir_menu():
    print("\n" + "="*30)
    print("🏥 Menu Gerenciador de Pacientes")
    print("="*30)
    print("1. Adicionar Novo Paciente")
    print("2. Exibir Todos os Pacientes")
    print("3. Análise de Dados (Média/Min/Max)")
    print("4. Buscar Paciente por Nome")
    print("5. Excluir Paciente")
    print("6. Sair")
    print("-" * 30)

def adicionar_paciente():
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
    if not pacientes:
        print("\nLista vazia. Cadastre um paciente primeiro (Opção 1).")
        return
        
    ordenados = sorted(pacientes, key=lambda x: x['idade'])
    
    print(f"\n--- Pacientes Cadastrados ({len(pacientes)} total) ---")
    for p in ordenados:
        
        print(f"Nome: {p['nome'].capitalize()} | Idade: {p['idade']} | Tel: {p['telefone']}")

def analise_dados():
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

def excluir_paciente():
    global pacientes
    
    if not pacientes:
        print("\nLista vazia. Cadastre um paciente primeiro (Opção 1).")
        return

    print("\n--- Excluir Paciente ---")
    nome_excluir = input("Digite o nome do paciente que deseja excluir: ").strip().lower()
    
    pacientes_antes = len(pacientes)
    
    pacientes = [p for p in pacientes if p['nome'] != nome_excluir]

    pacientes_depois = len(pacientes)
    
    if pacientes_depois < pacientes_antes:
        removidos = pacientes_antes - pacientes_depois
        print(f"✅ {removidos} paciente(s) com o nome '{nome_excluir.capitalize()}' removido(s) com sucesso.")
    else:
        print(f"❌ Paciente com o nome '{nome_excluir.capitalize()}' não encontrado.")

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-6): ")
        
        if escolha == '1':
            adicionar_paciente()
        elif escolha == '2':
            exibir_pacientes()
        elif escolha == '3':
            analise_dados()
        elif escolha == '4':
            buscar_paciente()
        elif escolha == '5':
            excluir_paciente()
        elif escolha == '6':
            
            print("Obrigado por utilizar o Gerenciador de Pacientes da Clinica Vida Plena. Até logo!)")
            sys.exit(0)
        else:
            print("❌ Opção inválida. Por favor, escolha um número entre 1 e 6.")

if __name__ == "__main__":
    main()