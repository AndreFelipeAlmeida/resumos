# QUESTÃO

2. Considere a seguinte parte de uma API de sistemas de arquivos.
```java
class File {
    // retorna o tamanho atual do arquivo
    long size();

    // escreve o array buffer no fim do arquivo. retorna a qtd de bytes escritos
    int append(byte[] buffer);
}
```

Note que a função append altera o objeto File enquanto a função size não o altera.

APIs desse tipo podem retornar valores inconsistentes caso uma thread que está realizando uma alteração (append) execute ao mesmo tempo que outra thread (que essa outra realize alterações ou não). Implemente o controle de concorrência (usando condvars ou semáforos) para esse objeto de forma a garantir que:

Qualquer número de threads possam executar concorrentemente a função size;

Threads que alteram o objeto (append) executem de maneira exclusiva (ou seja, nenhuma outra thread pode executar append ou size).

# RESPOSTA

```java
public class File {

    private final Semaphore mutex = new Semaphore(1);
    private final Semaphore writeLock = new Semaphore(1);
    private int readers = 0;

    public void size() {
        mutex.acquire();
        if (readers == 0) {
            writeLock.acquire();
        }
        readers++;
        mutex.release();

        /*
        * OPERAÇÃO DE SIZE
        */

        mutex.acquire();
        readers--;
        if (readers == 0) {
            writeLock.release();
        }
        mutex.release();
    }

    public void append(Runnable writeOperation) throws InterruptedException {
        writeLock.acquire();

        /*
        * OPERAÇÃO DE ADIÇÃO
        */

        writeLock.release();
    }
}
```