class Pessoa():
    def __init__(self):
        self.nome = {}
        self.idade = {}
        self.profissao = {}
        print('construtor chamado')
    def presentation(self):
        print('Oi, meu nome é %s, tenho %d anos de idade e sou %s' %(self.nome, self.idade, self.profissao))


pessoa = Pessoa()
pessoa.nome = input('Informe seu nome: ')
pessoa.idade = int(input('Informe sua idade: '))
pessoa.profissao = input('Informe sua profissão: ')
pessoa.presentation()
