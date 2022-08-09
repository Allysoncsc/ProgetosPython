from datetime import datetime
from re import I
from random import randint

class Pessoa:
    #pega o ano atual, Y= ano completo / y = os dois ultimos digitos do ano
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    #parametro self não precisa ser enviado
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar, pois está comendo')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de comer')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome}  está falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True




    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
    #metodo global da classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(1000, 1999)
        return rand