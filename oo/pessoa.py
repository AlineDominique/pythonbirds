class Pessoa:
    '''
    O atributos de instância de objetos são criados atraves do método especial __init__.
     Em python é possível criar atributos em tempo de execução para um objeto, mas este atributo é apenas para o objeto
     em que foi relacionado, nem um outro obejto do mesmo tipo terá este atributo. Como exemplo na linha 30.
     Atributo de Classe ou Default é usado quando um valor será igual em todos os objetos. Exemplo na linha 8,9.

    '''
    olhos = 2
    boca = 1
    '''
    Método de Classe: está relacionado a classe e não a instância. Ele pode ser acessado tanto pela Classe quanto por sua 
    instância, como mostrado na linha 74. Funciona como os atributos de classe.
    Para criar metodos de classe há 2 formas, usando decoretor @staticmethod ou @classmethod, sendo o último para acessar
    dados da própria Classe.
    
    '''
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls}'

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
        return f'Olá, meu nome é {self.nome}'

'''Herança Simples  
    Todos os atributos de dados e métodos da classe Mãe/Pai são herdados por suas
    classes filhas(os).
'''
class Mulher(Pessoa):
    def cumprimentar(self):
        '''
        o metodo super(): sempre retornará o resultado da classe pai.
        '''
        cumprimentar_ola = super().cumprimentar()
        return f'{cumprimentar_ola}. Aperto de Mão.'
'''
    Sobrescrita de Atributo: Exemplo com a Classe Mutante.
'''
class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    aline = Mulher(nome='Aline')
    mutante= Mutante(nome='Mutante')
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
    '''
    Atributos de Classe podem ser acessados pela própria classe e/ou pelo seus objetos. Exemplo linha 49 e 50.
    Obs: O __dict__ apenas retona os atributos de instâncias, os atributos de classe não.
    Forma de acesso aos atributos:
        Verifica-se o atributo é de instância, criados no __init__.
        Em caso de não existir, verifica se é um atributo da Classe.
    '''
    print(Pessoa.olhos)
    print(maria.boca)
    print(id(Pessoa.boca),id(maria.boca),id(aline.boca))
    maria.olhos = 3
    print(maria.__dict__)
    print(Pessoa.olhos, aline.olhos, maria.olhos)
    del maria.olhos
    print(maria.__dict__)
    print(Pessoa.olhos,aline.olhos,maria.olhos)
    print(id(Pessoa.olhos),id(aline.olhos),id(maria.olhos))

    print(Pessoa.metodo_estatico(),aline.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), aline.nome_e_atributos_de_classe())

    '''Método isinstance: este método retorna um booleano True: se o objeto é do tipo
     do segundo argumento e False: se o objeto é não é do tipo. Abaixo exemplo:'''
    anonimo = Pessoa('Anonimo')
    print(isinstance(anonimo,Pessoa))
    print(isinstance(anonimo,Mulher))
    print(isinstance(aline, Pessoa))
    print(isinstance(aline, Mulher))
    print(aline.olhos)
    print(mutante.olhos)
    print(aline.cumprimentar())
    print(mutante.cumprimentar())