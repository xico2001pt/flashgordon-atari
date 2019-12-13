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
1. ~**COLISÃO NO MAPA**~
   1. Não deixar nave mover se for contra alguma parede no mapa
   1. Quando chega a um rescue, desenhar 5 inimigos no ecrã de cima
      * Usar aleatoriedade para decidir o tipo de inimigo e a direção do movimento
      * Remover rescue point correspondente
   1. Transportar o jogador quando este chega aos extremos
1. ~**COLISÃO ECRÃ DE CIMA**~
   1. A nave não deve ultrapassar o ecrã
   1. Quando existe colisão da nave com inimigo, o jogador perde uma vida
   1. Nave pode disparar
   1. Quando existe colisão tiro com inimigo, o inimigo e o tiro desaparecem
1. ~**DESENHAR VIDAS**~
   * Implementar sistema de vida do jogador
   * Adicionar tempo de recuperação após perder uma vida
   * O nível termina quando não existem mais vidas
1. ~**CONSOLA**~
   1. Aspetos Gráficos
   1. Botões
      * Reset: Começar o jogo de novo
      * FPS: Configurar FPS do jogo
   1. Visor
      * Pontuação
      * Vidas
1. **MENU**
   * Ao iniciar o jogo deve ser apresentada uma tela inicial
1. **RESTART**
   1. Opção para reiniciar partida
   1. Todos os rescue points coletados
      * O jogo reinicia mantendo a pontuação, vidas e aumentando a velocidade dos inimigos
   1. A partida termina
      * São apresentadas as pontuações da partida atual e da mais elevada de todas as partidas realizadas
1. **EFEITOS SONOROS**
   * Todas as ações realizadas devem ter um som associado
1. **BÓNUS: TORNADO**
   * Área com grande concentração de inimigos
   * Caso não esteja nesta área, inimigos devem surgir aleatoriamente com pouca frequência

18/11/2019
