# l = [0, 1, 2,
#      3, 4, 5,
#      6, 7, 8]

# 4 = 3 * [1] + [1]
# 7 = 3 * [2] + [1]

class Velha:
  # linha = quociente
  # coluna = resto
  def __init__(self) -> None:
    self.jogo = [ ]
    for i in range(3):
      self.jogo.append([])
      for j in range(3):
        self.jogo[i].append(' ')

  def vazias(self): # retorna casas disponiveis
    disponiveis = [ ]
    
    for linha in range(3):
      for coluna in range(3):
        if self.jogo[linha][coluna] == ' ':
          celula = 3 * linha + coluna
          disponiveis.append(celula)
    
    return disponiveis
  
  def joga(self, celula, jogador):
    linha = celula // 3
    coluna = celula % 3

    self.jogo[linha][coluna] = jogador
    return self    

  # [i][i], [i][n-i-1]
  def ganhador(self):
    if self.jogo[0][0] == self.jogo[0][1] and self.jogo[0][1] == self.jogo[0][2]:
      return self.jogo[0][0] if self.jogo[0][0] != ' ' else False
    elif self.jogo[1][0] == self.jogo[1][1] and self.jogo[1][1] == self.jogo[1][2]:
      return self.jogo[1][1] if self.jogo[1][1] != ' ' else False
    elif self.jogo[2][0] == self.jogo[2][1] and self.jogo[2][1] == self.jogo[2][2]:
      return self.jogo[2][0] if self.jogo[2][0] != ' ' else False
    elif self.jogo[0][0] == self.jogo[1][0] and self.jogo[1][0] == self.jogo[2][0]:
      return self.jogo[0][0] if self.jogo[0][0] != ' ' else False
    elif self.jogo[0][1] == self.jogo[1][1] and self.jogo[1][1] == self.jogo[2][1]:
      return self.jogo[0][1] if self.jogo[0][1] != ' ' else False
    elif self.jogo[0][2] == self.jogo[1][2] and self.jogo[1][2] == self.jogo[2][2]:
      return self.jogo[0][2] if self.jogo[0][2] != ' ' else False
    elif self.jogo[0][0] == self.jogo[1][1] and self.jogo[1][1] == self.jogo[2][2]:
      return self.jogo[0][0] if self.jogo[0][0] != ' ' else False
    elif self.jogo[0][2] == self.jogo[1][1] and self.jogo[1][1] == self.jogo[2][0]:
      return self.jogo[0][2] if self.jogo[0][2] != ' ' else False
    
    return False
  
  def __str__(self) -> str:
    aux = ''
    primera_linha = True
    
    
    for linha in range(3):
      if primera_linha:
        primera_linha = False
      else:
         aux += '\n---+---+---\n'
      
      primeira_coluna = True
      for coluna in range(3):
          if primeira_coluna:
            primeira_coluna = False
          else:
            aux += '|'
            
          aux += f' {self.jogo[linha][coluna]} '
      
    return aux

l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
v = Velha()
it = 0

while len(v.vazias()) > 0 and it < 9:

  # (number % 2 == 1) == 0 (testa se eh pah)
  if it & 1 == 0:
    v = v.joga(l[it], 'X')
  else:
    v = v.joga(l[it], '0')
    
  it += 1
  if v.ganhador() != False:
    break


print(v, end=' ')
if v.ganhador() == False:
  print('Deu empate')
else:
  print('Ganhador: ', v.ganhador())