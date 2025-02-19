# EM BUSCA DE SOLUÇÕES

1. [BUSCA HEURÍSTICA](#busca-heurística)
---

## BUSCA HEURÍSTICA
- Heurística: Informação específica do domínio que pode ser usada para guiar o processo de busca
- Em muitos casos, heurística envolve uma função que avalia um nó particular e prediz a qualidade dos seus sucessores
- Heurísticas são aplicadas em problemas de IA em duas situações:
    - O problema não tem uma solução exata por causa de ambiguidades inerentes na formulação ou por causa da disponibilidade de dados
    - O problema tem solução exata, mas o custo computacional para encontrá-la é caro demais
- Heurísticas podem falhar
- A heurística é baseada na experiência e na intuição
- Uma heurística pode levar um algoritmo de busca a não encontrar a solução ou encontrar uma solução subótima

### Estratégias de Busca Heurística
- Usam conhecimento específico do problema na busca da solução
- Mais eficientes do que a busca não informada
- Algoritmo geral: Busca pela Melhor Escolha/Caminho (BME)
    - Seleciona para expansão o nó que tiver o menor custo estimado até o objetivo, segundo uma função de avaliação
    - Tipicamente, a função de avaliação f(n) usa uma função heurística h(n) que calcula o custo estimado do caminho mais econômico do nó passado como parâmetro (n) até um nó objetivo
- Uma forma de uso da informação heurística sobre um problema consiste em computar estimativas numéricas para os nós no espaço de estados. Essa estimativa indica quanto um nó é promissor com relação ao alcance de um nó objetivo
- A ideia é continuar a busca a partir do nó mais promissor
- O BME usa esse princípio

### Pequenos Exemplos
- Busca do melhor caminho: refinamento da busca em largura
- Busca em largura: sempre escolhe para expansão os menores caminhos-candidatos (nós extremos menos profundos da busca)
- Busca do melhor caminho: refina este princípio calculando uma estimativa heurística para cada candidato e escolhe a expansão do melhor candidato de acordo com a estimativa

### Busca gulosa pela melhor escolha
- Tentar expandir o nó mais próximo à meta, na suposição de que isso provavelmente levará a uma solução mais rápida
- Avalia nós para expandir com base unicamente na função heurística: f(n) = h(n)
- Não é completa
    - Pode entrar em ciclos e não encontrar a solução se não detectar estados repetidos
    - Pode se perder em um caminho infinito e nunca retroceder para outras opções
- Não é ótima
    - A solução pode não ser a menos custosa
    -  Dependendo do problema e da qualidade da heurística a complexidade pode ter uma redução substancial

### Busca A*
- BME mais famoso
- Objetivo: Minimizar o custo total estimado da solução
- Função de avaliação: f(n) = g(n) + h(n)
    - g(n) = custo (distância) do nó inicial ao nó n
    - h(n) = custo (distância) estimada de n ao final
    - Assim, f(n) estima o custo da melhor solução passando por n
- A* expande o nó de menor valor de f na fronteira de espaço de estados
- Quando n é encontrado pelo processo de busca, tem-se o seguinte:
    - um caminho de i (início) para n já deve ter sido encontrado e o seu custo pode ser calculado como a soma dos custos dos arcos (arestas) no caminho, servindo de estimativa para g(n)
    - h(n) é um mero palpite baseado no conhecimento geral do algoritmo sobre o problema particular, pois o espaço entre n e um nó objetivo não foi explorado
    - Não existe um método universal para construção de h(n), pois depende do domínio do problema
- Desempenho do A*
    - A análise do caráter ótimo de A* é direta se for usada com **BUSCA EM ÁRVORE**: A* será ótima se h(n) for uma heurística admissível.
    - Consequência mais importante da consistência (também chamada monotonicidade) é: A* usando **BUSCA EM GRAFO** é ótima se h(n) é consistente.
    - A* é completa e ótima se h(n) for admissível e consistente
    - h admissível: nunca superestima o custo de atingir a meta (busca em árvore) h(n) <= g(n, o)
    - h consistente: (busca em árvore) h(n) <= c(n, a, n') + h(n'), ∀n, n'
        - n' é o nó sucessor de n, resultante da ação a
        - c(n, a, n') é o custo de sair de n e atingir n' por meio da ação a
    - A* é otimamente eficiente: nenhum outro algoritmo ótimo garante expandir menos nós que A*
    - Infelizmente há, na maioria das vezes, crescimento exponencial do número de nós com o comprimento da solução (complexidade temporal).
    - O maior problema é a complexidade espacial: A* armazena todos os nós gerados!
    - Assim, A* não é aplicável em muitos problemas de grande escala. Usa-se variantes que encontram soluções subótimas.

### Com memória limitada 
- IDA* (Iterative Deepening A*)
    - Igual ao aprofundamento iterativo, porém seu limite é dado pela função de avaliação e não pela profundidade
    - Necessita de menos memória que A*
- SMA*
    - O número de nós guardados em memória é fixado previamente

### Considerações finais
- Solução de problemas usando técnicas de busca heurística:
    - dificuldades em definir e usar a função de avaliação
    - não consideram conhecimento genérico do mundo (ou “senso comum”)
- Função de avaliação: compromisso (conflito) entre
    - tempo gasto na seleção de um nó e
    - redução do espaço de busca
- Achar o melhor nó a ser expandido a cada passo pode ser tão difícil
quanto o problema da busca em geral.