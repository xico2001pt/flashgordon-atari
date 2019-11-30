# Projeto "New Flash Gordon"
### FPRO/MIEIC, 2019/20
### Francisco Gonçalves Cerqueira (up201905337@fe.up.pt)
### 1MIEIC07 

#### Objetivo

Criar um clone com um aspeto mais recente do [Flash Gordon](http://www.free80sarcade.com/2600_Flash_Gordon.php) (Atari 2600) em Pygame.

#### Descrição

Neste jogo, o jogador terá de se movimentar ao longo de um labirinto, indicado na metade inferior, com o objetivo de eliminar todos os inimigos. Para isso, o jogador terá de gerir a sua atenção entre as duas metades do ecrã.
O jogador perde quando é atingido pelos adversários três vezes.

#### UI

![UI](https://github.com/xico2001pt/flashgordon-atari/blob/master/flash_gordon_ui.jpg)

#### Pacotes

- Pygame
- Random

#### Tarefas

1. ~**MATRIZ PARA O MAPA**~
   1. fazer uma matriz binária (tamanho do mapa=32x8), em que teremos:
      * vazio=0
      * parede=1
   1. Desenhar os objetos no ecrã
      * para já cada objeto deverá ter 25x25 porque assim vai ocupar 25*32=800 pixeis, que é um tamanho razoável
      * colocar pontos de rescue ao longo do mapa
1. ~**DESENHAR ECRÃ CIMA**~
   1. Desenhar nave
   1. Desenhar também no mapa
1. ~**TECLAS**~
   * Navegação da nave usando as teclas de cursor
1. **COLISÃO NO MAPA**
   1. Não deixar nave mover se for contra alguma parede no mapa
   1. Quando chega a um rescue, desenhar 5 inimigos no ecrã de cima
      * Recolher posição do jogador para decidir em qual lado os inimigos aparecem
      * Usar aleatoriedade para decidir a direção que se desloca
   1. Transportar o jogador quando este chega aos extremos
1. **COLISÃO ECRÃ DE CIMA**
   1. Quando existe colisão da nave com inimigo, o jogador perde uma vida
   1. Nave pode disparar
      * existe uma lista com posição dos tiros
      * existe outra lista com direcção dos tiros
      * usar esta informação para desenhar e mover os tiros em cada ciclo
   1. Quando existe colisão tiro com inimigo, o inimigo desaparece
1. **DESENHAR ESTRELAS / DESENHAR VIDAS**
   * Implementar sistema de vida do jogador
   * Adicionar tempo de recuperação após perder uma vida
   * O nível termina quando não existem mais vidas
1. **MENU**
1. **CONSOLA**
   1. Aspetos Gráficos
   1. Configurações
      * FPS: Configurar FPS do jogo
      * Style: Alterar o estilo e as cores do jogo
   1. Pontuação
      * Adicionar contador com a pontuação do jogador
1. **EFEITOS SONOROS + RESTART**
1. **BÓNUS: Tornado**

18/11/2019
