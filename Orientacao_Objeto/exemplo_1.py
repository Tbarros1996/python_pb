# Programção em Python Orientada a Objetos
# Programador Thiago Barros


#Exemplo 1 de Programa 


class exemplo(): # A classe exemplo é definida
    def __init__(self, a = 2, b = 3):
        self.a = a # Self representa o objeto que terá atributos da classe fora da região da classe
        self.b = b
        
    def soma(self,x):
         return self.a*x + self.b
     
objeto_1 = exemplo() # A instância da classe foi criada e o objeto 1 foi definido
# com base nos métodos e atributos da classe exemplo

print(objeto_1.a,objeto_1.b) # Como os atributos da classe exemplo já definiram os atributos
# o objeto (ou instância de classe ) objeto_1, logo quando chamamos os atributos do objeto
# no caso as variáveis a e b jã temos definida pois é algo herdado da classe (herança)

#Podemos chamar o metodo soma que está o objeto objeto_1


print(objeto_1.soma(7)) #Veja que o objeto objeto_1 possui um método de somar da qual
#foi herdado da classe exemplo
