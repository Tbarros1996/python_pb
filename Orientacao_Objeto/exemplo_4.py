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

1. Classe Triangulo: Crie uma classe que modele
um triangulo:

– Atributos: LadoA, LadoB, LadoC

– Métodos: calcular Perímetro, getMaiorLado;

Crie um programa que utilize esta classe. Ele deve
pedir ao usuário que informe as medidas de um
triangulo. Depois, deve criar um objeto com as
medidas e imprimir sua área e maior lado.

"""

class triangulo:
    
    lado_A = None
    lado_B = None
    lado_C = None
    
    def __init__(self,lado_A,lado_B,lado_C):
         
        self.lado_A = lado_A
        self.lado_B = lado_B
        self.lado_C = lado_C
    
    def perimetro(self):
        
        print (self.lado_B + self.lado_B +self.lado_C)
    
    def maior_lado(self):
        
        if self.lado_A > self.lado_B and self.lado_A > self.lado_C :
            print("A é o maior lado")
        elif self.lado_B > self.lado_A and self.lado_B > self.lado_C:
            print("B é o maior lado")
        else:
            print("C é o maior lado")

batata = triangulo(1,2,3)
batata.perimetro() 
batata.maior_lado()