# Programção em Python Orientada a Objetos
# Programador Thiago Barros


# Criando uma classe retângulo
# Lembre-se: Os métodos sempre se iniciam com o self
# pois para usar o "." para referenciar o método
# no objeto (instância de classe)

# Lembre-se que a palavra chave "return" só faz isso, ela retorna
# o valor de uma função para que o programador possa armazena-la
# ou colocala em alguma operação. Exemplo mt.sin(x)
# A função sin da biblioteca da sin retorna apenas o valor da 
# operação que está na função sin.


# Criando uma classe pessoa e criando um método para calcular o ano nascimento

class pessoa:
    nome = None 
    idade = None
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade   
    def ano_nascimento(self,ano_atual):
        return ano_atual - self.idade
        
        
thiago = pessoa('Thiago',21)
print(thiago.ano_nascimento(2021))