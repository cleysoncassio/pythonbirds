class Pessoa:
    olhos = 2
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
        juan.sobrenome = 'cassio'
        del juan.filhos
        juan.olhos = 1
        del juan.olhos
        print(juan.__dict__)
        print(cleyson.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(juan.olhos)
        print(cleyson.olhos)
        print(id(Pessoa.olhos), id(juan.olhos), id(cleyson.olhos))


