# EM BUSCA DE SOLUÇÕES

1. [ALGORITMOS GENÉTICOS](#algoritmos-genéticos) 

---

## ALGORITMOS GENÉTICOS
- Um ramo doss algoritmos evolucionários
- Uma técnica de busca baseada na evolução natural
- São vistos como técnicas heurísticas de otimização global
- Estados sucessores são gerados por meio da combinação de dois estados antecessores
- Os “sucessores” (descendentes) de um “estado” (organismo ou indivíduo) ocupam a próxima geração de acordo com o seu “valor” (adaptação ou fitness)

### Características
- Podem operar com uma codificação do conjunto de parâmetros ou com os próprios parâmetros
- Realizam a busca com uma população de soluções candidatas
- Utilizam informações de custo ou recompensa
- Utilizam regras de transição estocásticas, não determinísticas

### Nomeação
- Parâmetros são representados como genes em um cromossomo
- Os valores específicos de um gene são chamados de alelo do gene
- Um cromossomo representa um indivíduo, composto por uma configuração de alelos (solução de um problema)
- A posição de um gene num cromossomo corresponde a um locus gênico

### Funcionamento
- Inicia com um conjunto de k estados gerados aleatoriamente, chamado população
- Cada estado (indivíduo) é representado como uma cadeia sobre um alfabeto finito
- Indivíduos são avaliados por uma função de fitness (função de avaliação em AG)
    - É uma nota dada ao indivíduo na resolução do problema. 
    - Dada a generalidade dos AG, a função de avaliação, em muitos casos, é a única ligação verdadeira do programa com o problema real.
- Indivíduos selecionados geram novos indivíduos por meio de cruzamento e mutações
- Repete avaliação/seleção/cruzamento-mutação até que um indivíduo seja avaliado como adequado para solução


### Seleção
- O princípio básico do funcionamento dos AG é que um critério de seleção vai fazer com que, depois de muitas gerações, o conjunto inicial de indivíduos gere indivíduos mais aptos
- Uso de função objetivo como avaliação de aptidão
- A aptidão pode ser vista como uma nota que medeo quão boa é a solução codificada por um indivíduo
- Baseada no valor da função-objetivo do problema
- Métodos
    - Roleta
    - Torneio
    - Amostragem Universal Estocástica

### Método de Seleção: Roleta
- Aptidão usada para definir fatia
- Valor aleatório para selecionar cromossomo
- Processo repetido até gerar os n indivíduos necessários

### Método de Seleção: Torneio
- Escolha aleatória de m indivíduos
- Uso de função de aptidão para escolher o melhor
- Processo repetido até gerar os n indivíduos necessários

### Método de Seleção: Amostragem
- Método da roleta com n agulhas igualmente espaçadas
- Roleta é girada uma única vez

### Operadores Genéticos
- Recombinação (Cruzamento)
    - Merge entre dois ou mais indivíduos (n:1)
    - A maneira com que é feito depende da representação dos indivíduos:
        - Binária
        - Inteira
        - Ponto flutuante
        - Objetos Compostos
    - Acrescenta indivíduos à população
- Mutação
    - Ocorre na relação de 1:1
    - A maneira com que é feita depende da representação dos indivíduos:
        - Binária
        - Inteira
        - Ponto flutuante
        - Objetos Compostos
    - Não afeta o tamanho da população
    - Mudança aleatória de alelo
    - Taxa de mutação
        - Significativamente inferior a de cruzamento
- Tipos
    - Ponto Único
    - Dois Pontos
    - Multiponto

### Codificação
- Codificação Binária 
    - É a mais comum devido a sua simplicidade
    - Cada cromossomo é uma string de bits – 0 ou 1
- Codificação por permutação
    - Mais usado em problemas de ordenação
    -  Cada cromossomo é uma string de números que representa uma posição numa seqüência
- Codificação por valor
    - Usada em problemas nos quais valores mais complicados são necessários
    - Cada cromossomo é uma seqüência de valores

### Parâmetros Genéticos
- Tamanho da população
- Taxa de cruzamento
- Taxa de mutação
- Intervalo de geração
    - Percentual de renovação da população
- Critério de parada
    - Número de gerações
    - Convergência da função de aptidão na população
    - Não melhoria da aptidão do melhor indivíduo após um número de gerações

### Elitismo
- Um elemento que tenha maior aptidão do que outro tem também maior probabilidade de ser selecionado.
- Nada impede que seja selecionado o pior, perdendo-se assim talve o melhor elemento da população, que poderia levar a uma convergência mais rápida.
- Para tentar minimizar este possível problema, elitismo pode ser adicionado à seleção.
    - Percentual de indivíduos com melhor aptidão é mantido na nova geração.

### Considerações Finais
-  AG são técnicas probabilísticas, e não técnicas determinísticas.
- Iniciando um AG com a mesma população inicial e o mesmo conjunto de parâmetros é possível encontrar soluções diferentes a cada vez que se executa o programa.
- A recombinação eleva a qualidade da busca, pois oferece uma maior diversidade para a população de indivíduos 
- AG não são métodos de "hill climbing" (otimização local), logo não ficarão estagnados simplesmente pelo fato de terem encontrado um máximo local. 
- Eles se parecem com a evolução natural, que só porque encontrou um indivíduo que é instantaneamente o melhor de um certo grupo não deixa de “procurar” outros indivíduos ainda melhores. 