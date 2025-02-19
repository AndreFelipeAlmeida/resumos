# EM BUSCA DE SOLUÇÕES

1. [COMO ESCOLHER UMA BOA FUNÇÃO HEURÍSTICA h](#como-escolher-uma-boa-função-heurística-h)
2. [EFEITO DA EXATIDÃO DA HEURÍSTICA SOBRE O DESEMPENHO](#efeito-da-exatidão-da-heurística-sobre-o-desempenho)
3. [ESTRATÉGIAS GENÉRICAS PARA DEFINIR h](#estratégias-genéricas-para-definir-h)
4. [CONSIDERAÇÕES FINAIS](#considerações-finais)

---

## COMO ESCOLHER UMA BOA FUNÇÃO HEURÍSTICA h
- h depende de cada problema particular
- h deve ser admissível
    - não superestimar o custo real da solução

## EFEITO DA EXATIDÃO DA HEURÍSTICA SOBRE O DESEMPENHO
- Qualidada da função heurística: medida através do fator de expansão efetivo (b* ou fator de ramificação efetiva)
    -  b* - fator de expansão de uma árvore uniforme com N+1 nós e nível de profundidade d
        - N+1 = 1 + b* + (b*)2 + ... + (b*)d,
        - N = total de nós gerados pelo A* para um problema;
        - d = profundidade da solução.
- Mede-se empiricamente a qualidade de h a partir do conjunto de valores experimentais de N e d
    - Uma boa função heurística terá o b* muito próximo de 1
- É sempre melhor utilizar uma função heurística com valores mais altos do fator, desde que seja admissível e que o tempo para computá-la não seja muito grande
- h1 domina h2 -> h1(n) >= h2(n), ∀n no espaço de estados
    - ou seja, h1 é melhor que h2, pois possui menor fator de ramificação
- Caso existam muitas funções heurísticas para o mesmo problema, e nenhuma delas domine as outras, usa-se uma heurística composta:
    - h (n) = max(h1(n), h2(n),…,hm(n))

## ESTRATÉGIAS GENÉRICAS PARA DEFINIR h
1) Relaxar o problema (versão simplificada);
2) Usar informação estatística;
3) Identificar os atributos relevantes do problema e usar aprendizagem.

## CONSIDERAÇÕES FINAIS
- Problemas mais realistas complicam bastante a implementação e a análise da busca heurística, requerendo heurísticas múltiplas.
- O entendimento ganho de jogos simples pode ser generalizado para problemas como aqueles encontrados em sistemas especialistas, planejamento, controle inteligente e aprendizado.
- Porém, uma heurística simples não pode ser aplicada a todos os estados nestes domínios.