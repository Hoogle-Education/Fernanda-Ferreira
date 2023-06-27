class Dominos:
  def __init__(self, l) -> None:
    self.estoque = l
    self.mesa = []
    
  def compra(self):
    return self.estoque.pop(0)

  def coloca(self, peca, extremidade):
    peca_esq, peca_dir = peca
    
    if self.mesa == []:  
      self.mesa.append((peca_esq, peca_dir, 'horizontal'))
      return True
    
    def inverte(orientacao):
      return 'vertical' if orientacao == 'horizontal' else 'horizontal'
    
    POS_INICIO, POS_FIM = 0, -1
    pos_mesa = POS_INICIO if extremidade == 0 else POS_FIM
    mesa_esq, mesa_dir, orientacao_mesa = self.mesa[pos_mesa]
    
    if extremidade == 0:
      if mesa_esq == peca_dir:
        self.mesa.insert(0, (peca_esq, peca_dir, inverte(orientacao_mesa)))
        return True
      elif mesa_esq == peca_esq:
        self.mesa.insert(0, (peca_dir, peca_esq, inverte(orientacao_mesa)))
        return True
    else:
      if mesa_dir == peca_esq:
        self.mesa.insert(-1, (peca_esq, peca_dir, inverte(orientacao_mesa)))
        return True
      elif mesa_dir == peca_dir:
        self.mesa.insert(-1, (peca_dir, peca_esq))
        return True
      
    return False
  
  def imprime(self):
    espacos = ''
    for esquerda, direita, orientacao in self.mesa:
      if orientacao == 'horizontal':
        print(espacos, esquerda, direita, sep='')
        espacos += ' ' 
      else:
        print(espacos, esquerda, sep='')
        print(espacos, direita, sep='')
    
l = [(5,6), (1, 5), (2,2), (3,4), (0,4), (1,3)]
d = Dominos(l)
  

for i in range(6):
  p = d.compra()
  print('Compra: ', p)
  if d.coloca(p, 0) or d.coloca(p, 1):
    d.imprime()