from unittest import TestCase
from oo.carro import Motor
'''Como executar os testes no terminal: 
    - No diretor do projeto;
    - No terminal digite: python3 -m unittest discover <nome do diretorio do teste> '''
class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0,motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)