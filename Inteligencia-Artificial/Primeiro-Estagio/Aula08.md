# RESOLUÇÕES DE PROBLEMAS

1. [BUSCA COMPETITIVA](#busca-competitiva)
2. [MINIMAX](#minimax)
3. [PODA α-β](#poda-α-β)
4. [JOGOS NÃO DETERMINÍSTICOS](#jogos-não-determinísticos)

---

## BUSCA COMPETITIVA
### Decisões ótimas em jogos
- Em jogos de dois jogadores, têm-se as seguintes funções de avaliação para guiar o processo de busca:
    - MAX (JOGADOR)
    - MIN (OPONENTE)
- Um jogo pode ser definido como uma árvore de busca:
    - Estado inicial
    - Função sucessora
    - Teste de Objetivo/Término
    - Função de Utilidade
        - Dá um valor numérico para os estados terminais (exemplo: 0 empate, +1 vitória, -1 derrota)
- Ideia
    - Iniciar na posição corrente e usar o gerador de movimentos (função sucessora) para gerar o conunto de possíveis posições sucessoras
    - Aplicar uma função de avaliação nestas posições e simplesmente escolher a melhor jogada
- Meta do Agente inteligente: Escolher a jogada que maximize a chance de vitória, sabendo que na jogada seguinte o oponente vai querer maximizara chance de vitória dele (portanto, o agente quer minimizar as chances do oponente)

## MINIMAX
- Um método para minimizar a perda máxima possível
- Ele busca descobrir, entre os caminhos possíveis, um que levará a vitória
- Do ponto de vista de max, valores altos de utilidade são bons.
- O algoritmo minimax ajuda a encontrar a melhor jogada ao caminhas pelas opções válidas a partir do fim do jogo (estados terminais) na direção do início do jogo (estados iniciais)
-  A cada passo assume-se que o jogador A está tentando maximizar as chances de A ganhar, enquanto na próxima rodada o jogador B está tentando minimizar as chances disso acontecer (ao maximizar as chances de que ele próprio ganhe)

### Estratégias Ótimas
-  Dada uma árvore de jogo, a estratégia ótima pode ser determinada a partir do valor minimax de cada nó.
-  O valor minimax (para MAX) é a utilidade de MAX para cada estado, assumindo que MIN escolhe os estados mais vantajosos para ele mesmo (i.e. os estado com menor valor utilidade para MAX)

### O Algoritmo
- Primeiro, deve-se descer os 'nós' da árvore até chegar nos estados terminais, identificando em quais estados o jogador perdeu, empatou ou ganhou (avaliação da função de utilidade)
- Após isso, o algoritmo sobe um 'nó' e identifica de quem é o turno (jogador ou oponente)
- Caso seja o turno do oponente, o algoritmo guarda naquele nó o menor resultado da função utilidade  de suas respectivas ramificações (MIN)
- Caso for o turno do jogador, o algoritmo guarda o maior resultado de suas respectivas ramificações (MAX)
- O processo se repete até se chegar ao primeiro 'nó' da árvore

## PODA α-β
- Busca MINIMAX: número de estados do jogo é exponencial em relação ao número de movimentos
- Poda α-β
    - Calcular a decisão correta sem examinar todos os nós da árvore
    - Retorna o mesmo que o MINIMAX, porém nem sempre percorrendo todos os estados
- Essa técnica requer a manutenção de dois valores limites
    - um representando o limite inferior que um nó maximizante poderá receber em última instância (alfa)
    - outro representando o limite superior de valor que um nó minimizante poderá ter (beta)

## JOGOS NÃO DETERMINÍSTICOS
- O estudo de algoritmos para jogos com elemento aleatório é um passo em direção a métodos aplicados no mundo real
- Uma árvore de um jogo não determinístico deve incluir nós de acaso além de nós minimax.
- Ramificações que levam a cada nó de acaso denotam “jogadas de dados possíveis” (a probabilidade de cada mudança de estado não determinística)