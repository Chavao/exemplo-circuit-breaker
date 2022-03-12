### Instalando as dependências

```
make setup
```

Obs: Depende do Python e pip instalado


### Executar server1

```
make server1
```

### Executar server2

```
make server2
```

### Executar o consumidor que aplica o circuit breaker

```
make run
```

### Como testar?

Para testar, basta fazer chamadas para http://127.0.0.1:5000/ ou http://127.0.0.1:5000/second e depois parar (com Ctrl + C) o `server1` e/ou o `server2` e refazer as chamadas.

As chamadas exibirão a mensagem `Failed` por 5 vezes, então o circuito se abrirá e exibirá uma mensagem de uma implementação local.

Ele retentará conexão a cada 10 segundos, se nesse meio tempo o `server1` e/ou o `server2` estiver voltado, ele responderá normalmente, senão ficará por mais 10 segundos esperando.

Obs: Esses números estão definidos no arquivo [circuit.py](https://github.com/Chavao/exemplo-circuit-breaker/blob/master/circuit.py)

### Observação

O exemplo é o mais simples possível, a organização dos arquivos e nomes de métodos e variáveis não devem ser utilizadas dessa forma em produção.
E a condição de abertura do circuit breaker não está levando em consideração tipos de erros, portanto basta o `server1` e/ou o `server2` estarem parados para ele começar a levar em consideração para a abertura.

### Leitura

* http://martinfowler.com/bliki/CircuitBreaker.html
* https://github.com/fabfuel/circuitbreaker/tree/master