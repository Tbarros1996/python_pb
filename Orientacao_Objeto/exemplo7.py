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
4. Implemente uma classe Aluno, que deve ter os
seguintes atributos: nome, curso, tempoSemDormir
(em horas). Essa classe deverá ter os seguintes
métodos:


– estudar (que recebe como parâmetro a qtd de horas de
estudo e acrescenta tempoSemDormir )

– Dormir (que recebe como parâmetro a qtd de horas de
sono e reduz tempoSemDormir )

Crie um código de teste da classe, criando um objeto
da classe aluno e usando os métodos estudar e dormir.
Ao final imprima quanto tempo o aluno está sem
dormir

"""

class Aluno:
    
    nome = None
    curso = None
    tempo_sem_dormir = None
    
    def __init__(self,nome,curso,tempo_sem_dormir):
        
        self.nome = nome
        self.curso = curso
        self.tempo_sem_dormir = tempo_sem_dormir
        
    def estudo (self,tempo):
        print(f"E o tempo estudado foi de {tempo}")
        return self.tempo_sem_dormir + tempo
    
    def sono(self,tempo):
        print(f'E as horas estudadas foram de {tempo}')
        return self.tempo_sem_dormir - tempo


aluno_1 = Aluno('Thiago','Engenharia Mecânica', 15)
print(aluno_1.tempo_sem_dormir) #Retorna o atributo do objeto aluno 1
aluno_1.estudo(12)
aluno_1.sono(8)

