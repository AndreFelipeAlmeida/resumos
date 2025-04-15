# COM FOR

```java
public class Barrier {
    int count = 0;
    int total_threads;
    Semaphore mutex;
    Semaphore catraca;
    Semaphore catraca2;

    public Barrier(int n) {
        mutex = new Semaphore(1);
        catraca1 = new Semaphore(0);
        catraca2 = new Semaphore(1);
        total_threads = n;
    }

    public void wait() {
        mutex.wait();
        count++;
        if (count == total_threads) {
            catraca2.wait();
            for (int i = 0; i < total_threads; i++)
                catraca1.signal();
        }
        mutex.signal();
        catraca1.wait();
        
        mutex.wait();
        count--;
        if (count == 0) {
            catraca1.wait();
            for (int i = 0; i < total_threads; i++)
                catraca2.signal();
        }
        mutex.signal();
        catraca2.wait();
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
    Semaphore catraca2;

    public Barrier(int n) {
        mutex = new Semaphore(1);
        catraca1 = new Semaphore(0);
        catraca2 = new Semaphore(1);
        total_threads = n;
    }

    public void wait() {
        mutex.wait();
        count++;
        if (count == total_threads) {
            catraca2.wait();
            catraca1.signal();
        }
        mutex.signal();

        catraca1.wait();
        catraca1.signal();

        mutex.wait();
        count--;
        if (count == 0) {
            catraca1.wait();
            catraca2.signal();
        }
        mutex.signal();
        
        catraca2.wait();
        catraca2.signal();
    }
}
```