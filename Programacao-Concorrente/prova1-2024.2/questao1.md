# QUESTÃO

1 - Crie um programa que recebe um número inteiro n, como argumento e cria n threads. Cada uma dessas threads deve executar uma função (void foo()). Esta função deve fazer duas coisas:

    1. Sortear um número aleatório (através da função int rand());

    2. Dormir por um tempo em segundos igual ao número aleatório sorteado (use a função sleep(int seconds) para isso).

A thread mãe deve criar as n threads filhas através da função create_thread(func, arg).

A thread mãe deve esperar que todas as filhas terminem de executar suas funções foo. Após as thread-filhas terminarem seu trabalho, a thread mãe deve retornar o maior e o menor valores entre os valores sorteados pelas threads filhas.

Implemente a função main e a função foo indicadas.

# RESPOSTA

```java
int maior = Integer.MIN_VALUE;
int menor = Integer.MAX_VALUE;
Semaphore mutex = new Semaphore(1);

void foo() {
    int valor = rand();
    sleep(valor);

    mutex.wait()
    if (valor > maior) maior = valor;
    if (valor < menor) menor = valor;
    mutex.signal()
}

int main(String args[]) {
    int n = args[0];

    Thread[] threads = new Thread[n];

    for (int i = 0; i < n; i++) {
        threads[i] = create_thread(foo); // Não sei o que é o parâmetro arg
        thread[i].start();
    }

    for (int i = 0; i < n; i++) {
        thread[i].join();
    }

    System.out.println("Maior valor: " + maior);
    printf("Menor valor: " + menor);
}

```