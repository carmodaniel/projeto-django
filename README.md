# Cadastro de Clientes - Sistema Django

Este projeto é uma aplicação Django moderna para gerenciar o cadastro de clientes e usuários, com layout responsivo, visual agradável e experiência de uso aprimorada. Desenvolvido como parte do curso de Python na Coderhouse.

## 🚀 Principais Funcionalidades

### **Gestão de Clientes**
- ✅ Cadastro, listagem, busca, edição e exclusão de clientes
- ✅ Busca por nome ou CNPJ com resultados em tempo real
- ✅ Estados brasileiros em formato select
- ✅ Confirmação de exclusão com modal responsivo
- ✅ Proteção de rotas: apenas usuários autenticados

### **Sistema de Usuários**
- ✅ Cadastro e login com validação avançada
- ✅ Regras de senha claras e validação em tempo real
- ✅ Upload e exibição de foto de perfil (ou avatar com inicial)
- ✅ Edição de perfil (e-mail e foto)
- ✅ Opção de deletar foto de perfil com confirmação
- ✅ Reset de senha para usuários

### **Gerenciamento Administrativo**
- ✅ Painel de gerenciamento para superusuários
- ✅ Bloquear/desbloquear usuários
- ✅ Reset de senha para outros usuários
- ✅ Exclusão de usuários com confirmação
- ✅ Lista completa de usuários com status

### **Interface e UX**
- ✅ Layout totalmente responsivo (desktop e mobile)
- ✅ Menu centralizado independente do logo
- ✅ Avatar do usuário sempre visível no cabeçalho
- ✅ Modal "Sobre Mim" com informações do projeto
- ✅ Modal "Leia mais" com dicas e FAQ
- ✅ Paleta de cores profissional e acessível
- ✅ Animações suaves e feedback visual

## 🎨 Paleta de Cores

- **Azul Escuro:** `#1A237E` (cabeçalho, botões principais)
- **Azul Claro:** `#42A5F5` (destaques, links, ícones)
- **Branco:** `#FFFFFF` (fundo principal, textos)
- **Cinza Claro:** `#F5F7FA` (fundo de cards, tabelas)
- **Cinza Médio:** `#B0BEC5` (bordas, divisores)
- **Verde Suave:** `#66BB6A` (status "Ativo", confirmações)
- **Vermelho Suave:** `#EF9A9A` (status "Inativo", alertas)

## 🛠️ Tecnologias Utilizadas

- **Backend:** Django 5.2.4 + Python 3.13
- **Frontend:** HTML5, CSS3 (customizado e responsivo)
- **Banco de Dados:** SQLite3
- **Upload de Imagens:** Pillow 11.3.0
- **Validação:** Django Forms com validação customizada
- **Autenticação:** Sistema nativo do Django

## 📱 Layout e Experiência

### **Cabeçalho e Navegação**
- Cabeçalho fixo com logo, nome do sistema e menu centralizado
- Menu responsivo que se adapta a diferentes tamanhos de tela
- Avatar do usuário sempre visível à direita (foto ou inicial)
- Botão "Leia mais" disponível no menu para todas as páginas

### **Modais Informativos**
- **"Sobre Mim":** Informações do desenvolvedor e projeto
- **"Leia mais":** Dicas de uso, FAQ e informações do sistema
- Ambos responsivos e com design consistente

### **Formulários e Validação**
- Validação de senha com regras claras
- Validação de nome de usuário (sem espaços, caracteres especiais)
- Mensagens de erro em português
- Feedback visual em tempo real

### **Responsividade**
- Adaptação perfeita para desktop, tablet e mobile
- Menu que se reorganiza em telas pequenas
- Cards e modais que se ajustam ao tamanho da tela
- Tipografia que mantém legibilidade em todos os dispositivos

## 🚀 Instalação e Execução

### **Pré-requisitos**
- Python 3.13+
- pip (gerenciador de pacotes Python)

### **Passos de Instalação**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/carmodaniel/projeto-django.git
   cd projeto-django
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\Activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   cd cadastro_clientes
   python manage.py migrate
   ```

5. **Crie um superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## 📁 Estrutura do Projeto

```
projeto-django/
├── cadastro_clientes/          # Projeto Django principal
│   ├── clientes/              # App de gestão de clientes
│   │   ├── models.py          # Modelos de dados
│   │   ├── views.py           # Lógica de negócio
│   │   ├── forms.py           # Formulários
│   │   ├── urls.py            # Rotas
│   │   └── templates/         # Templates HTML
│   ├── usuarios/              # App de gestão de usuários
│   │   ├── models.py          # Modelo Profile
│   │   ├── views.py           # Autenticação e perfil
│   │   ├── forms.py           # Formulários de usuário
│   │   └── templates/         # Templates de usuário
│   ├── static/                # Arquivos estáticos
│   │   └── style.css          # CSS principal
│   ├── media/                 # Upload de imagens
│   └── manage.py              # Script de gerenciamento
├── requirements.txt            # Dependências do projeto
├── .gitignore                 # Arquivos ignorados pelo Git
└── README.md                  # Este arquivo
```

## 🔧 Funcionalidades Detalhadas

### **Gestão de Clientes**
- **Listagem:** Tabela responsiva com todos os clientes
- **Cadastro:** Formulário com validação e campos obrigatórios
- **Edição:** Formulário pré-preenchido com dados atuais
- **Exclusão:** Confirmação modal antes de deletar
- **Busca:** Pesquisa por nome ou CNPJ em tempo real

### **Sistema de Usuários**
- **Cadastro:** Validação de senha forte e nome de usuário
- **Login:** Formulário limpo com validação
- **Perfil:** Edição de e-mail e upload de foto
- **Avatar:** Exibe foto ou inicial em círculo verde
- **Reset de Senha:** Funcionalidade completa

### **Gerenciamento (Admin)**
- **Lista de Usuários:** Tabela com status e ações
- **Bloquear/Desbloquear:** Controle de acesso
- **Reset de Senha:** Para qualquer usuário
- **Exclusão:** Com confirmação modal
- **Filtros:** Por status e tipo de usuário

## 🎯 Melhorias Recentes

### **UI/UX**
- ✅ Menu centralizado independente do logo
- ✅ Avatar responsivo no cabeçalho
- ✅ Modal "Leia mais" com informações do sistema
- ✅ Confirmações de exclusão com modais
- ✅ Validação visual em tempo real
- ✅ Feedback claro para todas as ações

### **Funcionalidades**
- ✅ Gerenciamento completo de usuários
- ✅ Upload e gerenciamento de fotos de perfil
- ✅ Estados brasileiros no cadastro de clientes
- ✅ Busca avançada de clientes
- ✅ Sistema de permissões aprimorado

### **Técnicas**
- ✅ Validação customizada de formulários
- ✅ Proteção de rotas com decorators
- ✅ Upload de imagens com Pillow
- ✅ Templates responsivos e acessíveis
- ✅ CSS moderno e organizado

## 🔒 Segurança

- **Autenticação:** Sistema nativo do Django
- **Proteção de Rotas:** Decorators `@login_required`
- **Validação:** Formulários com validação customizada
- **Upload Seguro:** Validação de tipos de arquivo
- **CSRF Protection:** Ativo em todos os formulários

## 📱 Responsividade

O sistema é totalmente responsivo e funciona perfeitamente em:
- **Desktop:** 1920px+
- **Laptop:** 1366px+
- **Tablet:** 768px+
- **Mobile:** 320px+

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Desenvolvedor

**Daniel Eduardo do Carmo**
- Analista de Sistemas
- Projeto desenvolvido para o curso Python Coderhouse

## 📞 Contato

- **GitHub:** [carmodaniel](https://github.com/carmodaniel)
- **Projeto:** [projeto-django](https://github.com/carmodaniel/projeto-django)

---

**Sinta-se à vontade para customizar, melhorar ou integrar este sistema com outros projetos!** 🚀

