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
5. Classe carro: Implemente uma classe chamada Carro com as
seguintes propriedades:

•Um veículo tem um certo consumo de combus}vel (medidos em km / litro) e
uma certa quanFdade de combus}vel no tanque.

•O consumo é especificado no construtor e o nível de combus}vel inicial é 0.

•Forneça um método andar( ) que simule o ato de dirigir o veículo por uma
certa distância, reduzindo o nível de combus}vel no tanque de gasolina. Esse
método recebe como parâmetro a distância em km.

•Forneça um método obterGasolina( ), que retorna o nível atual de
combus}vel.

•Forneça um método adicionarGasolina( ), para abastecer o tanque.

•Faça um programa para testar a classe Carro. 

Exemplo de uso:

meuFusca = Carro(15); 

# 15 quilômetros por litro de combus}vel.

meuFusca.adicionarGasolina(20); 

# abastece com 20 litros de
combus}vel.

meuFusca.andar(100); 

# anda 100 quilômetros.
meuFusca.obterGasolina() 

# Imprime o combus}vel que resta no
tanque.

"""

from time import sleep



class carro:
    
    
    combustivel_inicial = 0
    
    consumo = None
    
    print("Carro Criado com Sucesso")
    
    
    
    def __init__(self,consumo):
        
        self.consumo = consumo
        
        
        
    
    def combustivel(self):
        
        print(f'Você Tem {self.combustivel_inicial} Litros')
        
        
        
    def abastecer(self,litros):
        
        print(f'A quantidade de Combustivel Atual é {self.combustivel_inicial}')
        
        print(f'A quantidade Abastecida é de {litros} Litros')
        
        self.combustivel_inicial = self.combustivel_inicial + litros
        
        print(f'A quantidade de combustivel agora é de {self.combustivel_inicial} Litros')
        
        
        
    def andar(self,distancia):
        
        consumo_final = distancia*self.consumo
        
        combustivel_no_tanque = self.combustivel_inicial - consumo_final
    
        distancia_maxima = self.combustivel_inicial*self.consumo
        
        self.combustivel_inicial = combustivel_no_tanque
        
        
        if self.combustivel_inicial == 0 :
            
            print("Tanque Vazio, Necessário Abastecer")
            
            
        elif distancia_maxima < distancia and consumo_final > combustivel_no_tanque:
            
            print("Quantidade de Combustível Insuficiente para a Execução do Percurso")
            
             
        
        else :
            
            print(f"Com o combustível atual é possivel andar por apenas {distancia_maxima} KM") 
            
            print(f'Você deseja andar por {distancia}, [KM]')
            
            print('*')
            
            sleep(2)
            
            print('**')
            
            sleep(2)
            
            print('***')
            
            sleep(2)
            
            print('****')
            
            sleep(2)
            
            print('*****')
            
            sleep(2)
            
            print(f'Você Chegou no seu Destino')
            
            print(f'Você andou por {distancia} Km  e o combustível que restou no tanque é de {self.combustivel_inicial} Litros')
            
        
        
ferrari = carro(12)
ferrari.combustivel()
ferrari.abastecer(12)
ferrari.combustivel()
ferrari.andar(1)
ferrari.combustivel()

