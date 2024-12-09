# Sincronização de Relógios em Rede de Nós

Este projeto implementa um sistema de sincronização de relógios em uma rede distribuída de nós, onde cada nó comunica com seus vizinhos em um anel para calcular e atualizar o tempo médio de todos os nós. A coordenação do sistema é realizada por um nó com o maior ID, que é eleito por meio da troca de mensagens.

## Descrição

A rede é composta por um conjunto de nós interconectados em um anel. Cada nó tem um relógio local que pode estar desincronizado com os outros nós. O objetivo é calcular o tempo médio de todos os nós na rede e sincronizá-los. O nó com o maior ID se torna o coordenador, responsável por calcular e disseminar o tempo médio para os outros nós.

Quando um nó recebe uma mensagem com um timestamp, ele a propaga até que a mensagem retorne ao nó originador. Quando a mensagem retorna, o nó originador delega a coordenação ao nó anterior, calcula o tempo médio da rede e atualiza todos os nós com esse tempo.

## Funcionalidades

- **Criação e registro de nós**: Nós podem ser registrados na rede, criando um anel de comunicação.
- **Sincronização de relógios**: Os nós trocam mensagens para calcular e propagar o tempo médio.
- **Coordenação de rede**: O nó com o maior ID se torna o coordenador, responsável pela atualização do tempo de todos os nós.
- **Eleição do coordenador**: A eleição do coordenador é feita com base no maior ID entre os nós.
- **Falhas e reconexões**: O sistema lida com falhas de comunicação entre os nós, tentando reconectar ou contornar erros.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação usada para implementar a solução.
- **XML-RPC**: Protocolo de comunicação entre os nós da rede.
- **Threading**: Execução simultânea de servidores para cada nó.

## Como Executar

### Pré-requisitos

- Python 3.x instalado em seu sistema.
- Dependências:
  - `xmlrpc.server`
  - `xmlrpc.client`
  - `threading`
  - `datetime`

### Passos para Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/sync-time-network.git
   cd sync-time-network
