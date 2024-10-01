# sistema_bancario_simples
Sistema bancário simples em Python, permitindo realizar operações de depósito, saque e consulta de extrato. Ideal para iniciantes, este projeto ajuda a praticar lógica de programação e manipulação de dados, simulando funcionalidades reais de um banco de forma acessível e educativa.

# Sistema Bancário em Python

Este é um projeto iniciante de um sistema bancário simples desenvolvido em Python. Ele permite ao usuário realizar operações bancárias como **depositar**, **sacar** e **ver o extrato** de sua conta.

## Funcionalidades

- **Depositar**: Permite ao usuário adicionar fundos à conta bancária.
- **Sacar**: Permite ao usuário retirar fundos, desde que haja saldo suficiente.
- **Ver extrato**: Exibe o histórico de transações e o saldo atual.

## Pré-requisitos

- Python 3.x instalado. Você pode baixar a última versão [aqui](https://www.python.org/downloads/).

## Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/sistema-bancario-python.git
```

2. Navegue até o diretório do projeto:

```bash
cd sistema-bancario-python
```

3. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

4. Instale as dependências (se houver um arquivo `requirements.txt`):

```bash
pip install -r requirements.txt
```

5. Execute o sistema:

```bash
python main.py
```

## Como Usar

O sistema funciona no terminal. Ao iniciar, você terá três opções principais:

1. **Depositar**: Adicione um valor ao saldo da conta.
2. **Sacar**: Retire um valor, caso o saldo seja suficiente.
3. **Ver extrato**: Veja o saldo atual e todas as transações realizadas.

### Exemplo de Execução

```bash
Bem-vindo ao Sistema Bancário!
1. Sacar
2. Depositar
3. Ver Extrato
4. Encerrar

Escolha uma opção: 2
Digite o valor a ser depositado: 100
Depósito realizado com sucesso!

Escolha uma opção: 3
Extrato:
Depósito: R$ 100.00
Saldo atual: R$ 100.00
```

## Estrutura do Projeto

```bash
.
├── main.py               # Arquivo principal do sistema bancário
└── README.md             # Este arquivo
```

## Contribuindo

Contribuições são bem-vindas! Se você deseja melhorar o projeto, siga os passos abaixo:

1. Faça um _fork_ do projeto.
2. Crie uma nova _branch_ para suas alterações (`git checkout -b feature-nova-funcionalidade`).
3. Faça o _commit_ das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. _Push_ para a sua _branch_ (`git push origin feature-nova-funcionalidade`).
5. Abra um _pull request_.

## Licença

Este projeto está licenciado sob a [Nome da Licença] - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
