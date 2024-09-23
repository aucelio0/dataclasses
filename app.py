from modulo import *

if __name__ == "__main__":
    usuario = Pessoa('Mateus',21,1.76)

    usuario.nome = input('Informe seu nome: ')
    usuario.idade = int(input('Informe sua idade: '))
    usuario.altura = float(input('Informe sua altura: ').replace(',','.'))

    print(str(usuario))
