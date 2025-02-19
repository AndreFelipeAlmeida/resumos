# EM BUSCA DE SOLUÇÕES

1. [TIPOS DE PROBLEMAS](#tipos-de-problemas)
2. [BUSCA EM TODO O ESPAÇO DE ESTADOS](#busca-em-todo-o-espaço-de-estados)
3. [ESPAÇO DE ESTADOS DO PROBLEMA](#espaço-de-estados-do-problema)
4. [ESTRATÉGIA DE BUSCA](#estratégia-de-busca)
5. [ESTRATÉGIAS DE BUSCA CEGA](#estratégias-de-busca-cega)
6. [OBSERVAÇÕES](#observações)

---

## TIPOS DE PROBLEMAS
- Determinístico, totalmente observável
    - Problema de único estado
    - O agente sabe exatamente em qual estado estará e a solução é uma sequência de estados
- Não Observável
    - Problema conformante
    - Sensores estão ausentes ou não dão acesso a qualquer informação do ambiente
    - O agente pode não saber onde está
    - Mas uma solução pode ser encontrada
- Não determinístico e/ou parcialmente observável
    - Problema de contigência
    - Percepções fornecem novas informações sobre o estado corrente e a solução é um plano de contigência
    - Normalmente intercala busca e execução
- Espaço de Estados Desconhecido
    - Problema de exploração/descoberta ("online")

## BUSCA EM TODO O ESPAÇO DE ESTADOS
- Uso de uma árvore de busca explícita, gerada pelo estado inicial e a função de sucessor
- Uso de um grafo de busca, no qual o mesmo estado pode ser alcançado por vários caminhos

## ESPAÇO DE ESTADOS DO PROBLEMA
- Um problema pode ser visto como uma tripla? {I,O, B}
    - I: Estados Iniciais
    - O: Conjunto de Soluções
    - B: Estado Objetivo
- Uma solução para o problema é uma sequência finita de operaçõesque permite sair de um estado de I e chegar em um elemento em B

- Um sistema de resoluções de problemas é formado por:
    - Um conjunto de estruturas de dados organizada em um grafo
    - Um conjunto de operadores caracterizados por suas condições de aplicação e o que ele faz
    - Uma estrutura de controle implementando a estratégia de resolução 

## ESTRATÉGIA DE BUSCA
- Abordagens de busca básicas em um espaço de estados
    - Busca Cega
        - Não tem informação sobre qual sucessor é mais promissor para atingir a meta
    - Busca Heurística
        - Possui informação (estimativa) de qual sucessor é mais promissor para atingir a meta
        - É uma busca cega com um guia ou orientação
- Estratégias de busca são distinguíveis pela ordem em que os nós são expandidos

## ESTRATÉGIAS DE BUSCA CEGA
- Busca em Profundidade
    - Começa na raiz e avança para baixo em níveis cada vez mais profundos
    - Busca Vertical
    - Um operador é aplicado a um nó para gerar o próximo nó mais profundo
    - O processo continua até atingir um nó terminal/folha que é ou não solução. Quando não for solução, um retrocesso é forçado
    - Garante uma solução
    - A busca pode ser muito demorada, pois muitas ramificações diferentes podem ser expandidas até um nível muito profundo antes de uma solução ser encontrada
- Busca em Largura
    - Os nós em cada nível da árvore são completamente examinados antes de se mover para o próximo nível
    - A busca sempre encontrará o menor caminho possível, com relação a número de passos
    - Pode ter um limite de profundidade fixo imposto, para evitar que espaço de estados muito profundo sejam altamente expandidos. Porém, pode não encontrar o objetivo
- Aprofundamento Iterativo
    - Funciona como busca em profundidade, mas o algoritmo impõe um limite de profundidade
    - Até que o objetivo seja alcançado, a busca é repetida com o limite incrementado em 1

## OBSERVAÇÕES
- Critérios importantes na análise de um algoritmo de busca:
    - Completeza: O algoritmo oferece a garantia de encontrar uma solução quando ela existir?
    - Otimização: A estratégia encontra a solução ótima (tem o menor custo de caminho entre todas as soluções)?
    - Complexidade de tempo: Quanto tempo ele leva para encontrar uma solução?
    - Complexidade de espaço: Quanto de memória é necessário para executar a busca
- Explosão combinatorial: quando o número de alternativas a serem exploradas é tão grande que o problema de complexidade torna-se crítico.
- O número de caminhos candidatos à solução é exponencial com relação ao seu comprimento.
- Em se tratando de memória utilizada, na busca em profundidade é preciso armazenar todos os filhos não visitados de cada nó entre nó atual e nó inicial.
- Na busca em largura, antes de examinar nó a uma profundidade d, é necessário examinar e armazenar todos os nós a uma profundidade d - 1.
- Busca em profundidade utiliza menos memória. Quanto ao tempo, a busca em profundidade é geralmente mais rápida.
- Métodos de busca cega não examinam a árvore de forma ótima, apenas fazem uma busca exaustiva dentro do seu espaço. Para isso, pode-se empregar métodos heurísticos.