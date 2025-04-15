# QUESTÃO
3 - Considere a implementação de um sistema de processamento de requisições que funciona
no modo **master/worker**. Neste tipo de sistemas, temos duas entidades distintas: 1) um
**master** (chamado abaixo de broker); e 2) **workers**. O broker é a entidade para a qual
requisições são submetidas. Os workers são entidades que processam requisições. A API do
broker tem duas funções, listadas abaixo:

    type Broker
        void submitRequest(Request r);
        Request getWork(); // capacity

Considere que o Broker tem capacidade finita (**N**). Threads diferentes podem chamar a função
**submitRequest**. O Broker mantém as requests submetidas em um vetor de tamanho N. Workers
são threads que retiram requests do Broker através da função **getWork**. Caso tenha sido
submetido muitos requests, a ponto de o vetor de requests encher sua capacidade, threads
que submeter requests devem bloquear até que requests tenham sido retiradas. Por sua
vez, workers devem bloquear caso não tenhamos requests disponíveis. Uma request
submetida precisa ser processada por um único worker.

Considere a seguinte API para o worker:

    class Worker(Broker broker);

    run();
    void exec(Request req);

No método run, o worker deve executar em um loop infinito. O worker precisa retirar uma
Request do broker (chamando **getWork**) e depois executar o request com a função **exec**
(que você não precisa implementar).

Considere que:
1. threads serão criadas para executar os workers, portanto não se preocupe com isso;
2. Você deve inicializar semáforos no main criado por você. Os semáforos podem
   ser passados no construtor dos objetos (você pode mudar os construtores
   para tanto);
3. A constante N é conhecida;
4. Você deve implementar todo o resto do código necessário para o sistema
   funcionar (pelo menos **submitRequest** e **getWork** do Broker bem como **run**
   do Worker)


# RESPOSTA

```java
class Request {
    private final String conteudo;

    public Request(String conteudo) {
        this.conteudo = conteudo;
    }

    public String getConteudo() {
        return conteudo;
    }
}

class Broker {
    private final ArrayList<Request> fila;
    private final int capacidade;

    private final Semaphore semaforoVaga;   // controla o espaço disponível
    private final Semaphore semaforoItem;   // controla o número de requests disponíveis
    private final Semaphore mutex; // lock para proteger a fila

    public Broker(int capacidade) {
        this.capacidade = capacidade;
        this.fila = new ArrayList<>();
        this.semaforoVaga = new Semaphore(capacidade); // começa com N vagas
        this.semaforoItem = new Semaphore(0);          // começa com 0 requests
        this.mutex = new Semaphore(1);
    }

    public void submitRequest(Request r) {
        semaforoVaga.wait(); // espera se não houver vaga
        mutex.wait();
        fila.add(r);
        mutex.signal();
        semaforoItem.signal(); // libera um worker
    }

    public Request getWork() {
        Request r;
        semaforoItem.wait();
        mutex.wait();
        r = fila.remove(0);
        mutex.signal();
        semaforoVaga.signal();
        return r;
    }
}


class Worker {
    private final Broker broker;

    public Worker(Broker broker) {
        this.broker = broker;
    }

    public void exec(Request req) {
        System.out.println("Executando: " + req.getConteudo());
    }

    public void run() {
        while (true) {
            Request req = broker.getWork();
            exec(req);
        }
    }
}

```