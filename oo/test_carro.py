class Motor(): # Definindo a classe " Motor"
    def __init__(self, v1=2, v2=4, v3=6,): #definindo atributo de velocidade V= Velocidade
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def ligado(self): # definindo atributo de status = 'ligado'
        print(f'sistema ligado')


    def acel_1 (self): # definindo atributo de status de partida ' acelerando'
        print(f'acelerando na velocidade:{self.v1}')


    def acel_2(self):  # definindo atributo de status de partida ' acelerando'
        print(f'acelerando na velocidade:{self.v2}')

    def acel_3(self):  # definindo atributo de status de partida ' acelerando'
        print(f'acelerando na velocidade:{self.v3}')

    def freando (self): # definindo o atributo de parada - status "frear'
        print(f'freando o motor')


class Direcao():

    def __init__(self, norte, sul, leste, oeste, ):
        self.norte = norte
        self.sul = sul
        self.leste = leste
        self.oeste = oeste

    def virar_esquerda_1(self):
        self.norte = 1
        print('virar a esquerda sentido norte')

    def virar_a_direita_2(self):
        self.sul = 2
        print('virar a direita sentido sul')

    def virar_esquerda_3(self):
        self.leste = 3
        print('virar a direita sentido leste')

    def virar_a_direita_4(self):
        self.oeste = 4
        print('virar a direita sentido oeste')


if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao('norte', 'sul', 'leste', 'oeste', )
    motor.ligado()
    motor.acel_1()
    motor.acel_2()
    motor.acel_3()
    direcao.virar_esquerda_1()
    direcao.virar_a_direita_2()
    direcao.virar_esquerda_3()
    direcao.virar_a_direita_4()
    motor.freando()