# QUESTÃO
1. Três tipos de threads acessam uma lista encadeada. Threads de busca (executam a função search), de inserção (executam a função insert) e de remoção (executam a função delete). As threads de busca não modificam a lista, portanto podem ser executadas simultaneamente com outras do mesmo tipo. A função insert adiciona novos itens no final da lista. Por esse motivo, threads de inserção precisam executar de maneira mutuamente exclusiva. No entanto, uma inserção pode prosseguir concorrentemente com qualquer número de threads de busca. Por fim, a função delete remove itens de qualquer lugar na lista. Neste caso, somente uma thread de remoção pode executar por vez (a remoção também precisa ser exclusiva com inserção e busca). Implemente esse protocolo de concorrência.

# RESPOSTA

```java
import java.util.concurrent.Semaphore;

public class ListaConcorrente {

    private final Semaphore mutex = new Semaphore(1);
    private final Semaphore insertLock = new Semaphore(1);
    private final Semaphore deleteLock = new Semaphore(1);

    private int nSearchers = 0;

    public void search() {
        mutexSearchers.acquire();
        if (nSearchers == 0) {
            deleteLock.acquire();
        }
        nSearchers++;
        mutexSearchers.release();

        /*
        * OPERAÇÃO DE LEITURA
        */

        mutexSearchers.acquire();
        nSearchers--;
        if (nSearchers == 0) {
            deleteLock.release();
        }
        mutexSearchers.release();
    }

    public void insert() {
        insertLock.acquire();

        /*
        * OPERAÇÃO DE ADIÇÃO
        */

        insertLock.release();
    }

    public void delete() throws InterruptedException {
        deleteLock.acquire();
        insertLock.acquire();

        /*
        * OPERAÇÃO DE REMOÇÃO
        */

        insertLock.release();
        deleteLock.release();
    }
}

```