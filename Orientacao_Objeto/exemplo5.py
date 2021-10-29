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
2. Classe Funcionário: 

Implemente a classe
Funcionário. 

Um funcionário tem um nome e um
salário. 

Escreva um construtor com dois parâmetros
(nome e salário) e o método aumentarSalario
(porcentualDeAumento) que aumente o salário do
funcionário em uma certa porcentagem. Exemplo de
uso:
h
arry=funcionário("Harry",25000)
harry.aumentarSalario(10)

Faca um programa que teste o método da classe.


"""

class funcionario():
    nome = None
    salario = None
    
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def aumentarSalario(self,valor):
        x = self.salario*(1 + (valor)/100)
        print(f"O Salário foi aumentado em {valor}%, o que totalizou um novo salário de " , round(x,2),"Créditos")
        return x

funcionario_1 = funcionario("Thiago",1200)
funcionario_1.aumentarSalario(12)




