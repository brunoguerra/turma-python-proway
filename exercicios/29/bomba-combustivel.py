class BombaCombustivel:
  def __init__(self):
    self._tipo = 'gasolina'
    self._valor_litro = 0.0
    self._quantidade_combustivel = 0

  def abastecer_por_valor(self, valor):
      litros = valor / self._valor_litro
      self._quantidade_combustivel = self._quantidade_combustivel - litros
      print('Litros abastecidos: ', litros)

  def abastecer_por_litro(self, litros):
      self._quantidade_combustivel = self._quantidade_combustivel - litros
      print('Valor total a pagar: ', self._valor_litro*litros)

  def altera_valor(self, valor):
    self._valor_litro = valor

  def altera_combustivel(self, combustivel):
    self._tipo = combustivel
  
  def altera_quantidade(self, quantidade):
    self._quantidade_combustivel = quantidade

  def get_quantidade_restante(self):
    return self._quantidade_combustivel


class Posto:
  def __init__(self):
    self._bombas = []
  
  def add_bomba(self, bomba):
    self._bombas.append(bomba)
  
  def get_bombas(self):
    return self._bombas

meu_posto = Posto()

bomba_combustivel_gasolina = BombaCombustivel()
bomba_combustivel_gasolina.altera_combustivel('gasolina')
bomba_combustivel_gasolina.altera_valor(4.30)
bomba_combustivel_gasolina.altera_quantidade(1000)

meu_posto.add_bomba(bomba_combustivel_gasolina)

bomba_combustivel_alcool = BombaCombustivel()
bomba_combustivel_alcool.altera_combustivel('alcool')
bomba_combustivel_alcool.altera_valor(3.98)
bomba_combustivel_alcool.altera_quantidade(2000)

meu_posto.add_bomba(bomba_combustivel_gasolina)

bomba_combustivel_gasolina.abastecer_por_litro(55)
print('bomba combustivel gasolina possui', bomba_combustivel_gasolina.get_quantidade_restante(), 'litros restantes')