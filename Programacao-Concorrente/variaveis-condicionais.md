### O que são Variáveis Condicionais?
São mecanismos de sincronização usados junto com locks para permitir que uma thread:
* Espere por uma condição específica (tipo: "só posso continuar quando X acontecer")

* Seja acordada quando essa condição for satisfeita por outra thread

Elas não armazenam estado por si só, apenas ajudam a controlar o fluxo de execução baseado em condições lógicas.

### API
```java
    cv_wait(cond, mutex)	// Faz a thread esperar até ser acordada e libera o mutex
    cv_signal(cond)	// Acorda uma thread que está esperando em cond
    broadcast(cond)	// Acorda todas as threads esperando
```
Essas operações devem sempre ser usadas junto com um lock/mutex.

### EXEMPLO
```java
public class ProducerConsumer {

    private final Semaphore mutex = new Semaphore(1);
    private final VarCond cond1 = new VarCond(); // Não sei como se chama a classe
    private final VarCond cond2 = new VarCond(); // Não sei como se chama a classe
    private int numItems = 0;
    private int capacidade;
    private int max_loops;
    // ATRIBUTO BUFFER

    public ProducerConsumer(int capacidade, int max_loops) {
        this.capacidade = capacidade;
        this.max_loops = max_loops;
    }

    public void producer()  {
        for (int i = 0; i < max_loops; i++) {
            mutex.wait();
            while (numItems == capacidade) {
                cv_wait(cond1, mutex);
            }
            /*
            * PRODUÇÃO E ADIÇÃO NO BUFFER
            */
            numItens++;
            cv_signal(cond2);
            mutex.signal();
        }
    }

    public void consumer() {
        for (int i = 0; i < max_loops; i++) {
            mutex.wait();
            while (numItems == 0) {
                cv_wait(cond2, mutex);
            }
            /*
            * RETIRADA DO BUFFER E CONSUMO
            */
            numItems--;
            cv_signal(cond1)
            mutex.signal();
        }
    }
}
```

### Por que usar while?
Porque uma thread pode ser acordada sem motivo (spurious wakeup). Então a boa prática é sempre verificar a condição em um while, e não em um if.

### Diferença com semáforos puros
Semáforos contam os recursos disponíveis e controlam o acesso. Já as variáveis condicionais, por si só, não mantêm estado — elas servem apenas para bloquear e acordar threads em condições específicas.

