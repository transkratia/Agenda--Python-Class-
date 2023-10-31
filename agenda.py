class Agenda:
    def __init__(self, nome, email, telefone, idade, endereço):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade
        self.endereço = endereço

# Crio as listas para as funções funcionarem.

cadastros = []

# Crio a função de cadastro.

def Cadastrar():
    nome = input("Digite o nome completo: ")
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone: ")
    idade = int(input("Digite a idade: "))
    endereço = input("Digite o endereço: ")

    cadastro = Agenda(nome, email, telefone, idade, endereço)
    cadastros.append(cadastro)
    print("Cadastrado com sucesso!")

# Função para buscar cadastros por nome.

def buscarNome():
    achou = False
    acharNome = input("Digite o nome para buscar: ")
    for n in cadastros:
        if n.nome == acharNome:
            print("Nome encontrado, exibindo outros dados: ")
            print(f"E-mail: {n.email}.")
            print(f"Telefone: {n.telefone}.")
            print(f"Idade: {n.idade}.")
            print(f"Endereço: {n.endereço}.")
            achou = True
    if not achou:
        print("Nenhum cadastro encontrado com este nome.")

# Função para buscar cadastros por e-mail.

def buscarEmail():
    achou = False
    acharEmail = input("Digite o e-mail para buscar: ")
    for e in cadastros:
        if e.nome == acharEmail:
            print("E-mail encontrado, exibindo outros dados: ")
            print(f"Nome: {e.nome}.")
            print(f"Telefone: {e.telefone}.")
            print(f"Idade: {e.idade}.")
            print(f"Endereço: {e.endereço}.")
            achou = True
    if not achou:
        print("Nenhum cadastro encontrado com este e-mail.")

# Crio o Menu. Perdão pela Lenny Face.

def Menu():
    print("Programa Agenda - v.1.0")
    print("="*40)
    print("1 - Cadastrar")
    print("2 - Buscar por Nome")
    print("3 - Buscar por E-mail")
    print("4 - Buscar por Telefone")
    print("5 - Listar em Ordem por Nome")
    print("6 - Listar em ordem por Email")
    print("7 - Listar Maiores de Idade ( ͡° ͜ʖ ͡°)")
    print("8 - Sair")
    print("="*40)
    numb = int(input("Digite o número de uma opção: "))
    if numb == 1:
        Cadastrar()
    elif numb == 2:
        buscarNome()
    elif numb == 3:
        buscarEmail()
    elif numb == 4:
        buscarTelefone()
    elif numb == 5:
        listar_ordemNome()
    elif numb == 6:
        listar_ordemEmail()
    elif numb == 7:
        listar_maiorIdade()
    elif numb == 8:
        exit()
    else:
        print("O número digitado não possuí opção correspondente. Reiniciando.")

# Executo o Menu em looping.

Repetir = True
while Repetir:
    Menu()
