# Programção em Python Orientada a Objetos
# Programador Thiago Barros


# Lembre-se: Os métodos sempre se iniciam com o self
# pois para usar o "." para referenciar o método
# no objeto (instância de classe)

# Lembre-se que a palavra chave "return" só faz isso, ela retorna
# o valor de uma função para que o programador possa armazena-la
# ou colocala em alguma operação. Exemplo mt.sin(x)
# A função sin da biblioteca da sin retorna apenas o valor da 
# operação que está na função sin.


# Detalhe importante, todo método TEM DOIS PARENTESES pois é o método, logo
# não se esqueça de chamar ele com os DOIS PARENTESES

"""
3. Crie uma classe Livro que possui os
atributos nome, qtdPaginas, autor e preço.
– Crie os métodos getPreco para obter o valor
do preco e o método setPreco para setar
um novo valor do preco.

Crie um codigo de teste

"""

class livro():
    nome = None
    paginas = None
    autor = None
    preco = None
    def __init__(self,nome,paginas,autor,preco):
        self.preco = preco
        self.paginas = paginas
        self.autor = autor
        self.nome = nome
    def getPreco(self,valor):
        self.preco = valor
    def setPreco(self):
        print(f"O novo preço é {self.preco}")
        return self.preco


livro_1 = livro("As viagens de guliver",450,"Jonathan Smith",50)
print(livro_1.nome)
livro_1.getPreco(250)
livro_1.setPreco()


