class Agenda:
    def __init__(self, nome, email, telefone, idade, endereço):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade
        self.endereço = endereço

    def capitalizar_nome(self, nome):
        nome = nome.capitalize()
        return nome

    def pegar_numero(self, endereço):
        númeroEndereço = int(filter(str.isdigit, endereço))
        return númeroEndereço

    def imprimir(self):
        resp = "====================="
        resp += f"Nome: {self.nome}"
        resp += f"E-mail: {self.email}"
        resp += f"Telefone: {self.telefone}"
        resp += f"Idade: {self.idade}"
        resp += f"Endereço: {self.endereço}"
        resp += "====================="
        return resp

# Crio as listas para as funções funcionarem.

cadastros = []

# Crio a função de cadastro.

def Cadastrar():
    nome = input("Digite o nome completo: ")
    email = input("Digite o e-mail: ")
    while "@" not in email:
        email = input("Digite um e-mail COM @: ")
    telefone = int(input("Digite o telefone: "))
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

# Função para buscar cadastros por telefone.

def buscarTelefone():
    achou = False
    acharTelefone = int(input("Digite o telefone para buscar: "))
    for t in cadastros:
        if t.nome == acharTelefone:
            print("Telefone encontrado, exibindo outros dados: ")
            print(f"Nome: {t.nome}.")
            print(f"E-mail: {t.email}.")
            print(f"Idade: {t.idade}.")
            print(f"Endereço: {t.endereço}.")
            achou = True
    if not achou:
        print("Nenhum cadastro encontrado com este telefone.")

# Função para listar nomes em ordem alfabética.

def listar_ordemNome():
    listaNomeada = []
    listaOrdenada = []
    for n in cadastros:
        listaNomeada.append(n.nome)
        listaOrdenada = sorted(listaNomeada)
    if len(listaOrdenada) != 0:
        print(f"Os nomes, em ordem alfabética, são: {listaOrdenada}")
    else:
        print("Não há nomes para colocar em ordem alfabética.")

# Função para listar e-mail em ordem alfabética.

def listar_ordemEmail():
    listaNomeada = []
    listaOrdenada = []
    for n in cadastros:
        listaNomeada.append(n.email)
        listaOrdenada = sorted(listaNomeada)
    if len(listaOrdenada) != 0:
        print(f"Os e-mail, em ordem alfabética, são: {listaOrdenada}")
    else:
        print("Não há e-mail para colocar em ordem alfabética.")

# Função para listar maiores de idade.

def listar_maiorIdade():
    listaNomeada = []
    listaOrdenada = []
    for n in cadastros:
        if n.idade >= 18:
            listaNomeada.append(n.nome)
        listaOrdenada = sorted(listaNomeada)
    if len(listaOrdenada) != 0:
        print(f"Os maiores de idade são: {listaOrdenada}")
    else:
        print("Não há maiores de idade.")

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

# Considerações finais: eu não entendi o que o senhor quis dizer com "Liste os dados do(s) objeto(s) de forma
# padronizada incluindo um sequencial  e o total de objetos retornados."
