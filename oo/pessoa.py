class Pessoa:
    def __init__(self,*filhos, nome=None, idade= 41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    cleyson = Pessoa(nome='Cleyson')
    juan = Pessoa(cleyson, nome= 'Juan')
    print(Pessoa.cumprimentar(juan))
    print(id(juan))
    print(juan.cumprimentar())
    print(juan.nome)
    print(juan.idade)
    for filho in juan.filhos:
        print(filho.nome)


