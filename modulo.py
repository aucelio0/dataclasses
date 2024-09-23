from dataclasses import dataclass

@dataclass
class Pessoa:
    # atributos
    #NOTE: os atributos com dataclass já são private por padrão, e já recebem métodos de acesso automaticamente
    nome: str
    idade: int
    altura: float

    def __str__(self):
        return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} metros de altura.'
    
    def __del__(self):
        return f'{self.nome} destruido com sucesso.'