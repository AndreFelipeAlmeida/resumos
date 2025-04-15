# COM FOR
```java
public class Barrier {
    int count = 0;
    int total_threads;
    Semaphore mutex;
    Semaphore catraca;

    public Barrier(int n) {
        mutex = new Semaphore(1);
        catraca = new Semaphore(0);
        total_threads = n;
    }

    public void barrier_wait() {
        mutex.wait();
        count++;
        if (count == total_threads) {
            for (int i = 0; i < total_threads; i++) {
                catraca.signal();
            }
        }
        mutex.signal();

        catraca.wait();
    }
}
```

# SEM FOR

```java
public class Barrier {
    int count = 0;
    int total_threads;
    Semaphore mutex;
    Semaphore catraca;

    public Barrier(int n) {
        mutex = new Semaphore(1);
        catraca = new Semaphore(0);
        total_threads = n;
    }

    public void wait() {
        mutex.wait();
        count++;
        if (count == total_threads) {
            catraca.signal();
        }
        mutex.signal();

        catraca.wait();
        catraca.signal();
    }
}
```