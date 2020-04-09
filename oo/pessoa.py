class Pessoa:
    '''
    O atributos de instância de objetos são criados atraves do método especial __init__.
     Em python é possível criar atributos em tempo de execução para um objeto, mas este atributo é apenas para o objeto
     em que foi relacionado, nem um outro obejto do mesmo tipo terá este atributo. Como exemplo na linha 30.
    '''
    def __init__(self,*filhos,nome=None, idade=None):
        '''
        Explicação  no video:
        :param nome: refere-se a uma varável do contexto do código.
        :param self.nome: é nome do objeto self
        :param filhos: um atributo complexo
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
    maria.sobrenome = 'Santos'
    print(maria.sobrenome)
    '''
    O atributo especial __dict__ mostra os atributos de instância do objeto, os criados no __init__ e os em tempo de execução.
    É possível remover atributos dinamicamente também, usando o método <del + objeto.atributo>. Exemplo linha:39.
    Apesar da linguagem oferecer manipulação dinamica dos atributos, não é uma boa pratica. E dever ser usado em ocasiões
    específicas.     
    '''
    print(maria.__dict__)
    print(aline.__dict__)
    del maria.idade
    print(maria.__dict__)