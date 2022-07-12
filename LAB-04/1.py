class Automovel:
 
    def produzirVeiculo(self, motor1, motor2, motor3):
        print(f'Veiculo automovel com motor = {motor1}, '
              f' motor = {motor2} and Height = {motor3}')
 
class Caminhao:
 
    def produzirVeiculo(self, motor1, motor2, motor3):
        print(f'Veiculo caminhao com motor = {motor1}, '
              f' Breadth = {motor2} and Height = {motor3}')

class Motocicleta:
 
    def produzirVeiculo(self, motor1, motor2, motor3):
        print(f'Veiculo motocicleta com motor = {motor1}, '
              f' Breadth = {motor2} and Height = {motor3}')
 
class Veiculo:
 
    def __init__(self, motor1, motor2, motor3, producingAPI):
        self._motor1 = eletrico
        self._motor2 = hibrido
        self._motor3 = combustao
        self._producingAPI = producingAPI
 
    def producao(self):
        self._producingAPI.produzirVeiculo(self._motor)
 
    def expancao(self, n):
        self._motor1 = self._motor1 * n
        self._motor2 = self._motor2 * n
        self._motor3 = self._motor3 * n

 
