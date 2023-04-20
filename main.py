tabuleiro = ["- 1 -","- 2 -","- 3 -","- 4 -","- 5 -","- 6 -","- 7 -","- 8 -","- 9 -"]
combinacoes = [[1,2,3], [1,5,9], [1,4,7], [2,5,8], [3,5,7], [3,6,9], [4,5,6], [7,8,9]]
jogador_X = []
jogador_O = []

def mostrarTabuleiro():
    print(5*"-"," Tabuleiro ",5*"-")
    index=0
    linha=[]
    cont=1
    for i in range(len(tabuleiro)):
        index+=1
        linha.append(tabuleiro[i])
        if index == 3:
            print(linha)
            linha.clear()
            index=0
            cont+=1

def verif(jogador):
  for x in combinacoes:
    cont=0
    for i in x:
      if i in jogador:
        cont+=1
    if cont == 3:
      if jogador == jogador_X:
        return "X"
      elif jogador == jogador_O:
        return "O"
  return ""
         
def rodada(jogador, valor):
  mostrarTabuleiro()
  print(5*"-",f"Jogador {valor}",5*"-")
  posicao = int(input("Qual posição deseja jogar:\n"))
  if tabuleiro[posicao-1] == f"- {posicao} -":
      tabuleiro[posicao-1] = f"- {valor} -"
      jogador.append(posicao)  
      if verif(jogador) == "X":
        return "X"
      elif verif(jogador) == "O":
        return "O"
  else:
    print("Por favor escolha uma posição livre!")
    rodada(jogador,valor)

def verifEmpate():
  cont=0
  for i in tabuleiro:
    if i == "- X -" or i == "- O -":
      cont+=1
    if cont == 9:
      print(5*"-"," Empate ",5*"-")
      return 0
    
def main():
  while True:
    rodada(jogador_X, "X")
    if verif(jogador_X) == "X":
      mostrarTabuleiro()
      print("O jogador X venceu!")
      break
    else:
      if verifEmpate() == 0:
        mostrarTabuleiro()
        break
    rodada(jogador_O, "O")
    if verif(jogador_O) == "X":
      mostrarTabuleiro()
      print("O jogador O venceu!")
      break
    else:
      if verifEmpate() == 0:
        mostrarTabuleiro()
        break   

main()
