# Programção em Python Orientada a Objetos
# Programador Thiago Barros


# Criando uma classe retângulo
# Lembre-se: Os métodos sempre se iniciam com o self
# pois para usar o "." para referenciar o método
# no objeto (instância de classe)

class retangulo(): # Nova classe Retângulo Criada
    lado_A = None # atributo 1 definido como sem valor
    lado_B = None # atributo 2 definido como sem valor
    def __init__(self,lado_A,lado_B): # Inicializador de atributos da classe
        self.lado_A = lado_A # Atributo 1 sendo referenciado para a novo objeto
        self.lado_B = lado_B
        print("Novo objeto Triângulo Criado")
        
    # Dois métodos são criados para calcular os
    # Atrubutos área e  perimetro
    
    def area(self): 
        return self.lado_A * self.lado_B
    def perimetro(self):
        return self.lado_A * 2 + self.lado_B * 2
    

# Criando a objeto

#Pense como matrix_1 = np.array([1,2,3],[4,5,6])
#Objeto matrix_1 da classe array criado com o método np


retangulo_batata = retangulo(1,2) #Perceba que a instância requer uma 
#entrada de argumento para a definição do objeto
print(retangulo_batata.lado_A, retangulo_batata.lado_B)

area = retangulo_batata.area()
perimetro = retangulo_batata.perimetro() 
print(area,perimetro)

# Lembre-se que a palavra chave "return" só faz isso, ela retorna
# o valor de uma função para que o programador possa armazena-la
# ou colocala em alguma operação. Exemplo mt.sin(x)
# A função sin da biblioteca da sin retorna apenas o valor da 
# operação que está na função sin.


