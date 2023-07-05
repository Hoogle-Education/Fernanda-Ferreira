class Ponto:
  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y
    
  def __repr__(self) -> str:
    return f'P({self.x}, {self.y})'
  
class Ciclo:
  
  def __init__(self, centro, raio) -> None:
    x, y = centro
    self.centro = Ponto(x, y)
    self.raio = raio
    
def ponto_in_ciclo(ciclo, ponto) -> bool:
  delta_x = (ciclo.centro.x - ponto.x) ** 2
  delta_y = (ciclo.centro.y - ponto.y) ** 2
  
  if (delta_x + delta_y)  >= ciclo.raio**2:
    return False
  
  return True

def rect_in_ciclo(ciclo, rect) -> bool:
  for ponto in rect:
    if not ponto_in_ciclo(ciclo, ponto):
      return False
  
  return True

circunferencia, t2 = eval(input())
centro, raio = circunferencia

to_verify = ()

if len(t2) == 4:
  a, b, c, d = t2
  rect = (a, b, c, d)
  print(rect_in_ciclo(circunferencia, to_verify))
else:
  ponto = t2
  print(rect_in_ciclo(circunferencia, ponto))
  
