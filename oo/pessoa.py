class Pessoa:
    '''
    O atributos de instância de objetos são criados atraves do método especial __init__.
    '''
    def __init__(self,*filhos,nome=None, idade=None):
        '''
        Explicação  no video:
        :param nome: refere-se a uma varável do contexto do código.
        :param self.nome: é nome do objeto self
        :param filhos: um atributo complexo,
        '''
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    aline = Pessoa(nome='Aline')
    maria = Pessoa(aline,nome='Maria Benedita')
    print(Pessoa.cumprimentar(maria))
    print(id(maria))
    print(maria.cumprimentar())
    print(maria.nome)
    print(maria.idade)
    for filho in maria.filhos:
        print(filho.nome)