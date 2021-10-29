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


# Criando uma classe conta corrente


class conta_corrente:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0
        
    def debitar(self,valor):
        return self.saldo - valor
    
    def creditar(self,valor):
        return self.saldo + valor


conta_do_jose = conta_corrente(12)
total_somado = conta_do_jose.creditar(12)
total_perdido = conta_do_jose.debitar(21)

print(total_somado,total_perdido)

