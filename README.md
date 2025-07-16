# Cadastro de Clientes

Este projeto é uma aplicação Django moderna para gerenciar o cadastro de clientes e usuários, com layout responsivo, visual agradável e experiência de uso aprimorada.

## Principais Funcionalidades

- Cadastro, listagem, busca, edição e exclusão de clientes
- Gerenciamento de usuários (admin pode bloquear, desbloquear, resetar senha e excluir usuários)
- Cadastro e login de usuários com validação avançada de senha e nome de usuário
- Upload e exibição de foto de perfil do usuário (ou avatar com inicial)
- Proteção de rotas: apenas usuários autenticados podem acessar funcionalidades de clientes
- Layout responsivo, minimalista e moderno, adaptado para desktop e mobile
- Cabeçalho fixo com menu centralizado (independente do logo) e avatar do usuário à direita
- Modal "Sobre Mim" acessível no menu principal, com conteúdo responsivo e leitura agradável
- Paleta de cores profissional e acessível
- Botões de ação compactos, lado a lado, com visual limpo

## Paleta de Cores

- **Azul Escuro:** #1A237E (cabeçalho, botões principais)
- **Azul Claro:** #42A5F5 (destaques, links, ícones)
- **Branco:** #FFFFFF (fundo principal, textos)
- **Cinza Claro:** #F5F7FA (fundo de cards, tabelas)
- **Cinza Médio:** #B0BEC5 (bordas, divisores)
- **Verde Suave:** #66BB6A (status "Ativo", confirmações)
- **Vermelho Suave:** #EF9A9A (status "Inativo", alertas)

## Layout e Experiência

- **Cabeçalho fixo:** com logo, nome do sistema, menu centralizado (não depende do tamanho do logo) e avatar do usuário à direita
- **Cards arredondados:** com sombra suave para agrupar informações (ex: formulários, tabelas)
- **Menu responsivo:** centralizado, quebra para coluna em telas pequenas, nunca ultrapassa a largura da página
- **Avatar do usuário:** exibe foto de perfil ou inicial, sempre visível e alinhado à direita
- **Botões de ação:** compactos, lado a lado, cores intuitivas e sem quebra de linha
- **Modal "Sobre Mim":** mais largo, leitura fácil, responsivo e sem barra de rolagem na maioria dos casos
- **Tipografia moderna:** Inter, Roboto ou Montserrat
- **Animações suaves:** para feedback de ações

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

## Estrutura do Projeto

- `clientes/` — Funcionalidades de clientes (CRUD, busca, templates)
- `usuarios/` — Cadastro, login, perfil, gerenciamento e templates de usuários
- `static/style.css` — CSS global com paleta, responsividade e layout moderno
- `templates/` — HTMLs minimalistas, responsivos e com visual profissional

## Observações

- O projeto utiliza Django 5+
- Todas as rotas de clientes exigem autenticação
- O layout é totalmente responsivo e acessível
- O avatar do usuário é exibido no cabeçalho após login
- O menu é centralizado e adaptável a qualquer tela
- O modal "Sobre Mim" está disponível em todas as páginas, com leitura confortável
- Dependências atualizadas no requirements.txt

---

Sinta-se à vontade para customizar o visual, adicionar novas funcionalidades ou integrar com outros sistemas!

