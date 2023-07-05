class Intervalo:
  
  def __init__(self, a, b) -> None:
    self.start = min(a, b)
    self.end = max(a, b)
    
  def __repr__(self) -> str:
    return f'Intervalo({self.start}, {self.end})'
    
  # [1, 2]U[5, 6]
  def intersecao(self, other):
    biggest = self if self.end > other.end else other
    smallest = self if self.end < other.end else other
    
    if biggest.start > smallest.end:
      raise ValueError('Não há interseção')
    
    common_start = max(self.start, other.start)
    common_end = min(self.end, other.end)
    return Intervalo(common_start, common_end)
  
  def uniao(self, other): 
    start = min(self.start, other.start)
    end = max(self.end, other.end)
    return Intervalo(start, end)
    
    
def adiciona(l, i):
  for k, j in enumerate(l):
    try:
      x = i.intersecao(j)
      l.pop(k)
      u = i.uniao(j)
      return adiciona(l, u)
    except ValueError:
      pass
    
  l.append(i)
  return l

#  ((4,1),(10,2),(2,10),((5,6),(7,9)))
e1, e2, e3, e4 = eval(input())


print(Intervalo(e1[0],e1[1]).uniao(Intervalo(e2[0],e2[1])))

try:
  print(Intervalo(e1[0],e1[1]).intersecao(Intervalo(e3[0],e3[1]))) 
except ValueError:
  # obs: Se der ValueError tem que imprimir "Deu bode", 
  # igual ao exemplo de uso.
  print('Deu bode')
  
l = [Intervalo(e1[0],e1[1])]

# para cada tupla i em e4 fazer l = adiciona(l, Intervalo(i[0],i[1])). 
# Depois de adicionas todos os intervalor em e4 imprimir l.
for i in e4:
  l = adiciona(l, Intervalo(i[0],i[1]))

print(l)