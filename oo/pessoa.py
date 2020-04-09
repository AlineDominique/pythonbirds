class Pessoa:
    '''
    O atributos de instância de objetos são criados atraves do método especial __init__.
    '''
    def __init__(self,nome=None, idade=None):
        '''
        Explicação  no video:
        :param nome: refere-se a uma varável do contexto do código.
        :param self.nome: é nome do objeto self
        '''
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    p = Pessoa('Dominique')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Aline'
    print(p.nome)
    print(p.idade)