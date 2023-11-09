class Cliente:
    def __init__(self, CPF, nome, email, telefone, endereço):
        self.nome = nome
        self.CPF = CPF
        self.email = email
        self.telefone = telefone
        self.endereço = endereço

class Carro:
    def __init__(self, modelo, marca, ano, preço, dono):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preço = preço
        self.dono = dono

    def aumentarPreco(self, valor):
        self.preco += (self.preco * valor) / 100

    def diminuirPreco(self, valor):
        self.preco -= (self.preco * valor) / 100


clientes = []
carros = []

def cadastrarCliente():
    nome = input("Digite o nome completo: ")
    email = input("Digite o e-mail: ")
    while "@" not in email:
        email = input("Digite um e-mail COM @: ")
    telefone = float(input("Digite o telefone: "))
    CPF = int(input("Digite o CPF: "))
    endereço = float(input("Digite o endereço: "))


    cadastro = Cliente(nome, email, telefone, CPF, endereço)
    clientes.append(cadastro)
    print("Cadastrado com sucesso!")

def cadastrarCarro():
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))
    preço = float(input("Digite o preço: "))
    dono = Cliente(input("Digite o dono: "))


    cadastro = Carro(marca, modelo, ano, preço, dono)
    carros.append(cadastro)
    print("Cadastrado com sucesso!")

def Menu():
    print("Programa Agenda - v.1.0")
    print("="*40)
    print("1 - Cadastrar cliente")
    print("2 - Cadastar carro")
    print("3 - Buscar carros por nome do cliente")
    print("4 - Buscar clientes por marca")
    print("5 - Listar todos os carros por cliente")
    print("6 - Sair")
    print("="*40)
    numb = int(input("Digite o número de uma opção: "))
    if numb == 1:
        cadastrarCliente()
    elif numb == 2:
        cadastrarCarro()
    elif numb == 3:
        buscarCarro()
    elif numb == 4:
        buscarCliente()
    elif numb == 5:
        listarCarro()
    elif numb == 6:
        exit()
    else:
        print("O número digitado não possuí opção correspondente. Reiniciando.")

# Executo o Menu em looping.

Repetir = True
while Repetir:
    Menu()
