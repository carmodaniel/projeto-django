# Cadastro de Clientes

Este projeto é uma aplicação Django desenvolvida para gerenciar o cadastro de clientes, com possibilidade futura de expansão para contratos e serviços. O sistema foi criado para fins didáticos no curso Coderhouse.

## Funcionalidades Atuais

- Cadastro de clientes com validação de CNPJ único
- Listagem de clientes em tabela estilizada
- Busca de clientes por nome ou CNPJ
- Edição e exclusão de clientes
- Interface amigável e responsiva

## Estrutura do Projeto

- `clientes/` — Aplicação principal, contém:
  - `models.py`: Modelos de Cliente, Contrato e Serviço (estes dois últimos para expansão futura)
  - `views.py`: Funções de listagem, criação, edição, exclusão e busca de clientes (e esqueleto para contratos/serviços)
  - `forms.py`: Formulários Django para validação dos dados
  - `templates/clientes/`: Templates HTML para as páginas do sistema
- `db.sqlite3` — Banco de dados SQLite padrão
- `requirements.txt` — Dependências do projeto

## Instalação e Execução

1. Clone o repositório:

   ```bash
   git clone <url-do-repositorio>
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Acesse a pasta do projeto e aplique as migrações:

   ```bash
   cd cadastro_clientes
   python manage.py migrate
   ```

4. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

5. Acesse `http://127.0.0.1:8000/` no navegador.

## Explicação do Código Python/Django

### Views (views.py)

- **Clientes**
  - `lista_clientes`: Lista todos os clientes cadastrados.
  - `cria_cliente`: Permite cadastrar um novo cliente. Valida se o CNPJ já existe e exibe mensagem de erro se necessário.
  - `atualiza_cliente`: Permite editar os dados de um cliente existente.
  - `deleta_cliente`: Exclui um cliente após confirmação.
  - `busca_cliente`: Permite buscar clientes por nome ou CNPJ, exibindo resultados em tabela. Se não encontrar, mostra mensagem adequada.

- **Contratos e Serviços**
  - As views para contratos e serviços (`lista_contratos`, `cria_contrato`, `atualiza_contrato`, `deleta_contrato`, `lista_servicos`, `cria_servico`, etc.) já estão estruturadas, mas a lógica de negócio e os templates podem ser expandidos conforme a necessidade futura.

### Models (models.py)

- `Cliente`: Armazena informações como nome, CNPJ, estado, situação, data de cadastro, etc. O campo CNPJ é validado para ser único.
- `Contrato` e `Servico`: Modelos preparados para futura implementação de cadastro, edição e exclusão.

### Forms (forms.py)

- `ClienteForm`: Formulário para cadastro/edição de clientes, com validação de CNPJ único.
- `BuscaClienteForm`: Formulário para busca de clientes por nome ou CNPJ.
- `ContratoForm` e `ServicoForm`: Formulários para futuras funcionalidades.

### Templates (templates/clientes/)

- Páginas HTML para cadastro, listagem, busca, edição e exclusão de clientes, com layout responsivo e mensagens de erro amigáveis.

## Observações

- O projeto utiliza Django 5+.
- Para customizações, edite os arquivos em `clientes/`.
- As funcionalidades de contratos e serviços podem ser expandidas facilmente, pois a estrutura já está preparada.

---

