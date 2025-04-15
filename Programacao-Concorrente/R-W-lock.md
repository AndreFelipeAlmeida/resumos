Um R/W lock (ou Read/Write lock, em português, "trava de leitura/escrita") é um tipo especial de mecanismo de sincronização usado em programação concorrente para controlar o acesso a recursos compartilhados, como variáveis, arquivos ou estruturas de dados, em ambientes com múltiplas threads.

## Ideia principal:
Permitir múltiplos leitores simultaneamente, mas garantir que somente uma thread possa escrever por vez, e nenhuma leitura aconteça durante a escrita.

```java
public class ReadWriteLock {

    private final Semaphore mutex = new Semaphore(1);
    private final Semaphore writeLock = new Semaphore(1);
    private int readers = 0;

    public void lockRead() {
        mutex.acquire();
        readers++;
        if (readers == 1) {
            writeLock.acquire();
        }
        mutex.release();
    }

    public void unlockRead() {
        mutex.acquire();
        readers--;
        if (readers == 0) {
            writeLock.release();
        }
        mutex.release();
    }

    public void lockWrite() {
        writeLock.acquire();
    }

    public void unlockWrite() {
        writeLock.release();
    }
}
```