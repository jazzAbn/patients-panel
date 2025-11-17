#criando uma lista vazia para armazenar os dados de pacientes uma expecie de array vazio.
pacientes = []
#AQUI eu utilizei o WHILE pq eu preciso que seja adcionado mais pacientes ate o usuario  decidir parar de adcionar mais pacietes
 
while True:
    nome = input("Nome do paciente: ") .lower()
    idade = int(input("Idade do paciente: "))
    telefone = input("Telefone do paciente: ")

    #.append e utilizado para adicionar novos elementos a lista inicial dentro de um dicionario com as informacoes iniciais do novo paciente
   
    pacientes.append({'nome': nome, 'idade': idade, 'telefone': telefone})
    
    continuar = input("Deseja adicionar outro paciente? (s/n): ").lower()
    if continuar.lower() != 's':
        break

#aqui estou criando um relatorio simples de todos os pacientes cadastrados 
print(f"Total de pacientes cadastrados: {len(pacientes)}")

#Calcular a média de idades de todos os pacientes
soma_idades = 0
for paciente in pacientes:
    soma_idades += paciente['idade']

media_idade = soma_idades / len(pacientes)
print(f"Média das idades: {media_idade:.2f} anos")


#selecionar o paciente mais novo e o mais velho dentro da lista de cadastro de pacientes 
#aqui o lambda estou comparando apenas o valor idade dentro do dicionario
mais_novo = min(pacientes, key=lambda x: x['idade'])
mais_velho = max(pacientes, key=lambda x: x['idade'])

#em cada printe estou formatando a str para inserir o nome e a idade do paciente mais novo e o mais velho da lista de pacientes cadastrados manualmente 
print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

#nesta parte eu crio uma ordedem crescente de idade dos pacientes cadastrados 
#sorted e utilizado para ordenar a lista de pacientes com base na idade do paciente mais novo para o mais velho 

ordenados = sorted(pacientes, key=lambda x: x['idade'])
print("\nPacientes ordenados por idade:")
for p in ordenados:
    print(f"{p['nome']} - {p['idade']} anos")

#Aqui eu crio uma busca simples por nome do paciente dentro da lista com um input para a digitação do nome 
buscar = input("\nDigite o nome do paciente que deseja localizar: ").lower()
encontrado = [p for p in pacientes if p['nome'].lower() == buscar]

#aqui eu crio uma condição de if para a busca do paciente e um for para printar os dados do paciente caso ele tenha sido encontrado no array de pacientes 
if encontrado:
    for p in encontrado:
        print(f"\nPaciente encontrado:\nNome: {p['nome']}\nIdade: {p['idade']}\nTelefone: {p['telefone']}")
else:
    print("Paciente não encontrado.")