# Projeto Flash Gordon
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

#### Tarefas

1. **MATRIZ PARA O MAPA**
   1. fazer uma matriz de inteiros (tamanho do mapa=32x8), em que teremos:
      * vazio=0
      * parede=1
      * rescue=2
   1. Desenhar os objetos no ecrã
      * para já cada objeto deverá ter 25x25 porque assim vai ocupar 25*32=800 pixeis, que é um tamanho razoável
1. **DESENHAR ECRÃ CIMA**
   1. Desenhar nave
       * Sugiro tentar manter o tamanho das coisas múltiplos de 25
       * Ou seja, a nave poderia ser 75x50
   1. Desenhar também no mapa
1. **TECLAS**
   * Navegação da nave usando as teclas de cursor
1. **COLISÃO NO MAPA**
   1. Não deixar nave mover se for contra alguma parede no mapa
   1. Quando chega a um rescue, desenhar 5 inimigos no ecrã de cima
1. **COLISÃO ECRÃ DE CIMA**
   1. Quando existe colisão nave com inimigo => perde uma vida
   1. Nave pode disparar
      * existe uma lista com posição dos tiros
      * existe outra lista com direcção dos tiros
      * usar esta informação para desenhar e mover os tiros em cada ciclo
   1. Quando existe colisão tiro com inimigo => inimigo desaparece
1. **DESENHAR ESTRELAS / DESENHAR VIDAS**
1. **MENU**

18/11/2019
