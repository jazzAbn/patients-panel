#lista de variaveis
lista_paciente = []
#menu principal
def menu_principal():
    print('----------MENU PRINCIPAL----------')
    print('(1) Cadastrar novo paciente')
    print('(2) Consultar paciente')
    print('(3) Editar paciente')
    print('(4) Excluir paciente')
    print('(0) Sair')
menu_principal()

#caso escolham uma opção diferente do menu
first_choise = int(input('Escolha a função desejada: '))
while first_choise < 0 or first_choise > 5:
    print('Opção inválida. Por favor, selecione uma das opções do menu.')
    first_choise = int(input('Escolha a função desejada: '))
else:
#fechar programa
    if first_choise == 0:
        print("Programa desenvolvido por @JazzAbn  Certificado de Garantia ISO NOVE MIL nenhum e ISO nem me viu depois.")
        import time, sys
        for i in range(0, 10):
            sys.stdout.write("\r{}".format(i))
            sys.stdout.flush()
            time.sleep(1)
        exit()
#cadastrar novo paciente 
    elif first_choise == 1:
        print('Cadastrar novo paciente.')
        ident = input('ID: ')
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        endereco = input('Endereço: ')
        print('{}, {}, {}'.format(nome, telefone, endereco))
        lista_paciente.append((ident, nome, telefone, endereco))
        cadastrar_de_novo = input('Deseja cadastrar novo paciente? [s/n]: ')
        while cadastrar_de_novo == 's':
            print('Cadastrar novo paciente.')
            ident = input('ID: ')
            nome = input('Nome: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')
            print('{}, {}, {}'.format(nome, telefone, endereco))
            lista_paciente.append((ident, nome, telefone, endereco))
            cadastrar_de_novo = input('Deseja cadastrar novo paciente? [s/n]: ')
        else:
            first_choise = menu_principal()
#consultar paciente
    elif first_choise == 2:
        print(lista_paciente)

    elif first_choise == 3:
        print('Consultar paciente.')

    elif first_choise == 4:
        print('Consultar paciente.')