# QUESTÃO

2 - Considere a implementação de um Pilha, que internamente usa vetores, com pelo menos a seguinte interface. Para este problema, considere que a pilha tem capacidade máxima definida em 1000 elementos.

```java
// cria uma pilha
new Stack();

// verifica se a pilha está vazia
boolean isEmpty();

// remove e retorna o item no topo da pilha
int pop();

// adiciona um novo item no topo da pilha
void push(int value);
```

Sua implementação deve ser correta considerando que um número arbitrário de threads usará a pilha concorrentemente.

Corretude é mais importante do que desempenho (embora desempenho também seja importante, ou seja, não proteja regiões desnecessariamente).
Você deve usar semáforos para desenvolver sua solução concorrente segura.

# RESPOSTA

```java
public class Stack {
    private static final int MAX = 1000;
    private final int[] data = new int[MAX];
    private int top = -1;

    private final Semaphore mutex = new Semaphore(1);

    public boolean isEmpty() {
        mutex.acquire();
        return top == -1;
        mutex.release();
    }

    public void push(int value) {
        mutex.acquire();
        if (top < MAX - 1) {
            data[++top] = value;
        } else {
            System.out.println("Erro: Pilha cheia!");
        }
        mutex.release();
    }

    public int pop() {
        mutex.acquire();
        if (top >= 0) {
            int value = data[top--];
            return value;
        } else {
            return -1;
        }
        mutex.release();
    }
}
```