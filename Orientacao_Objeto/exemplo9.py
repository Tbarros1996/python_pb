# Programação Orientada a Objetos
# Programador Thiago Barros


# Uso de Dockstring para documentar código

class Carro:
        
    '''
    
    Programação orientada a Objetos
    
    Classe Carros
    
    Atributos:   cor
                marca
                modelo
                nome
                fabricante
    
    Método:     andar()
                freiar()
                ligar_farol()
                desligar_farol()
                estado()
                
    
    '''
    
    cor = None
    
    modelo = None
    
    nome = None
    
    fabricante = None
    
    luzes = 0
    
    motor = 0
    
    ar_condicionado = 0
    
    radio = 0
    
    bancos_front  = [0  ,  0]
    
    bancos_back   = [0  ,  0]
    
    andando = 0
    
    def __init__(self,modelo,marca,cor,fabricante):
            
            self.marca = marca
            self.modelo = modelo
            self.cor = cor
            self.fabricante = fabricante
            self.bancos_back =  [0  ,  0]
            self.bancos_front = [0  ,  0]
           
           
    def dados(self):
            
            
            print({ "Marca do Veículo":
                    self.marca
                    
                ,
                    "Modelo do Veículo":
                            
                            self.modelo
                            
                ,
                            
                 "Cor":
                         
                        self.cor  
            })       
                
    def ligar_motor(self):
            
        if self.bancos_front[0] == 1:
                
                self.motor = 1
                
                print("O motor está ligado")
                
        elif self.bancos_front[0]== 0:
                
                print("Impossivel ligar o motor, necessário um motorista")
        

    def desligar_motor(self):
            
            self.motor = 0
            
            print("O motor está desligado")
        
        
    def ligar_radio(self):
            
            self.radio = 1
            
            print("O radio está desligado")
            
    def desligar_radio(self):
            
            self.radio = 0
            
            print("O radio está desligado")

        
        
    def desligar_ar(self):
            
            self.ar_condicionado= 0
            
            print("O ar condicionado está desligado")
            
            
    def ligar_ar(self):
            
            self.ar_condicionado = 1
            
            print("O ar está ligado")
            
    
    def andar(self):
            
        if self.bancos_front[0] == 0 and self.andando == 0:
                        
                        print("Impossível do carro andar, necessário 1 motorista")
                
        elif self.bancos_front[0] == 1 and self.andando == 0 and self.motor == 0:
                
                print("Carro ligado e andando")
                
                self.andando = 1
                
                self.motor = 1
        

    def desligar_radio(self):
            
            self.radio = 0
            
            print("O radio está desligado")
    
    def entrar_carro(self,banco):
        
        if self.andando == self.motor == 1:
                
                print("Impossível entrar no carro pois o mesmo está em movimento")    
        
        if self.andando == 0 and self.motor == 1 or self.andando == 0 and self.motor == 0:
                
            if self.banco == 1:
                    
                    print("Pessoa Está no Banco do Motorista")
                    
                    self.bancos_front[0] == 1
                    
            elif self.banco == 2:
                    
                    print("Pessoa Está no Banco 1")
                    
                    self.bancos_front[1] == 1
                    
            elif self.banco == 3:
                    
                    print("Pessoa Está no Banco do Passageiro atrás do Motorista")
                    
                    self.bancos_back[0] == 1
                    
            elif self.banco == 1:
                    
                    print("Pessoa Está no Banco do Passageiro 2")
                    
                    self.bancos_back[1] == 1 
                     
            elif self.banco == 1:
                    
                    print("Pessoa Está no Banco 1")
                    
                    self.bancos_front[0] == 1 
                    
    
    def sair_carro(self,banco):
            
        if self.andando == self.motor == 1:
                
                print("Impossível sair do carro pois o mesmo está em movimento")    
        
        if self.andando == 0 and self.motor == 1 or self.andando == 0 and self.motor == 0:           
            
            if self.banco == 1:
                    
                    print("Pessoa Está no Banco do Motorista")
                    
                    self.bancos_front[0] == 1
                    
            elif self.banco == 2:
                    
                    print("Pessoa Está no Banco 1")
                    
                    self.bancos_front[1] == 1
                    
            elif self.banco == 3:
                    
                    print("Pessoa Está no Banco do Passageiro atrás do Motorista")
                    
                    self.bancos_back[0] == 1
                    
            elif self.banco == 1:
                    
                    print("Pessoa Está no Banco do Passageiro 2")
                    
                    self.bancos_back[1] == 1 
                     
            elif self.banco == 1:
                    
                    print("Pessoa Está no Banco 1")
                    
                    self.bancos_front[0] == 1                       

    def estado_atual(self):
            
            if self.bancos_back == self.bancos_front == 0:
                    
                    if self.luzes == 0 and self.motor == 0 and self.radio == 0 and self.ar_condicionado == 0:
                            
                            print("O carro está Vazio e Desligado")
                            
                    elif self.luzes == 1 and self.motor == 0 and self.radio == 0 and self.ar_condicionado == 0:
                            
                            print("O carro está com as luzes acessas mas desligado, favor apague as luzes")
                            
                    elif self.luzes == 1 and self.motor == 1 and self.radio == 0 and self.ar_condicionado == 0:
                            
                            print("O carro está vazio mas com as luzes acesas e o rádio ligado, favor desligar")
                            
                    elif self.luzes == 1 and self.motor == 1 and self.radio == 1 and self.ar_condicionado == 0:
                            
                            print("O carro está com as luzes,motor e rádio ligados mas com a ar desligado")
                            
                            print("Favor, desligar caso esteja parado")
                    else:
                            print("O carro está todo ligado")

                
meuFusca = Carro("Fusca Itamar","Volks", "Preto","Volks do Brasil")
meuFusca.dados()
meuFusca.andar()
meuFusca.estado_atual()
meuFusca.entrar_carro(1)
            

    
        