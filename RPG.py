import random

class Personagem():
    def __init__(self, nome, vida, level = 1 ):
        self.nome = nome
        self.__vida = vida
        self.__level = level

    def receber_dano(self, dano):
        self.vida -= dano

    def atacar(self, alvo):
        if alvo == self:
            print('Você não pode atacar a si mesmo')
        elif self.__vida == 0:
            print('Não pode atacar. Personagem já morreu')
        else:
            ataque = random.choice(self.ataques)
            dano = random.randint(ataque['dano min'], ataque['dano max'])
            dano *= self.level
            alvo.receber_dano(dano)
            print(f'O personagem {self.nome}({self.vida}) é um {self.__class__.__name__}(LVL{self.level}), atacou o personagem {alvo.nome}({alvo.vida}) com o ataque {ataque['nome']} e deu {dano} de dano.')
           

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, valor):
        if 1 <= valor <= 10:
            self.__level = valor
        else:
            print('Level inválido')
   
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, valor):
        if self.__vida == 0 and valor > 0:
            print('Personagem já morto, não pode reviver')
        elif valor < 0:
            self.__vida = 0
        else:
            if 0 <= valor <= 3000:
                self.__vida = valor
            else:
                print('Vida inválida')
        
class Guerreiro(Personagem):
    ataques = [{
        'nome': 'Soco',
        'dano min': 20,
        'dano max': 50
    },
    {
         'nome': 'Espadada',
        'dano min': 60,
        'dano max': 120
    }]
        
class Arqueiro(Personagem):
    ataques = [{
        'nome': 'Flechada',
        'dano min': 50,
        'dano max': 90
    },
    {
        'nome': 'Flechada Flamejante',
        'dano min': 100,
        'dano max': 140
    }]

class Mago(Personagem):
    ataques = [{
        'nome': 'Bola de Vento',
        'dano min': 40,
        'dano max': 100
    },
    {
        'nome': 'Bola de Fogo',
        'dano min': 80,
        'dano max': 150
    },
    {
        'nome': 'Buraco Negro',
        'dano min': 300,
        'dano max': 500
    }]