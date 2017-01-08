class Livro():
	def __init__(self):
		self.nome  		= 'Narnia'
		self.autor 		= 'Clive Staples Lewis'
		self.edicao		= '1'
		self.lancamento	= '1950'
		print('Construtor chamado!')
	def sobre(self):
		print("O livro %s é do autor(a) %s e está na %sª edição com data de	lançamento em %s" %(self.nome,self.autor,self.edicao, self.lancamento))

narnia = Livro()
narnia.sobre()		