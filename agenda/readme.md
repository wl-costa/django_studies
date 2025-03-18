# Agenda - Aplicativo Django

## Descrição
Este projeto foi desenvolvido como parte dos meus estudos para um processo seletivo na **RedeBR**, onde precisei aprofundar meus conhecimentos em **Django** e criar uma aplicação funcional do zero. Durante esse período de aprendizado, explorei conceitos fundamentais do framework, desde a criação de modelos e views até a autenticação de usuários.

A aplicação **Agenda** permite que usuários cadastrados possam **gerenciar eventos pessoais** de forma segura e intuitiva. O sistema conta com **autenticação de usuários**, incluindo login via **Google OAuth**, garantindo que cada usuário visualize apenas seus próprios eventos.

Além disso, a aplicação segue boas práticas de desenvolvimento, incluindo modularização de páginas, uso do **Bootstrap** para estilização e o princípio **DRY** (Don't Repeat Yourself), tornando o código mais organizado e escalável.

## Funcionalidades

- **CRUD de eventos**: criar, visualizar, editar e excluir eventos.
- **Autenticação de usuários**:
  - Login e logout
  - Autenticação via Google OAuth
- **Segurança**: cada usuário só pode acessar e modificar seus próprios eventos.
- **Filtragem e pesquisa**:
  - Filtragem de eventos por intervalo de datas.
  - Pesquisa por título dos eventos.
- **Interface responsiva e estilizada** com Bootstrap, proporcionando uma boa experiência de usuário.

## Tecnologias utilizadas (Stack)

- **Linguagem:** Python 3.13.2
- **Framework:** Django 5.1.7
- **Banco de Dados:** SQLite
- **Ambiente Virtual:** venv
- **Autenticação Social:** Django Social Auth (Google OAuth2)
- **Frontend:** Templates HTML, CSS, Bootstrap

## Estrutura do Projeto

O projeto está estruturado da seguinte maneira:

```
agenda/
│── agenda/            # Configurações globais do projeto
│   ├── templates/     # Templates HTML para renderização das páginas
│   │   ├── agenda.html
│   │   ├── evento.html
│   │   ├── login.html
│   │   ├── model-footer.html
│   │   ├── model-header.html
│   │   ├── model-page.html
│   ├── settings.py    # Configurações do Django
│   ├── urls.py        # Rotas globais
│── core/               # Aplicação principal
│   ├── migrations/    # Arquivos de migração do banco de dados
│   ├── models.py      # Modelos do banco de dados
│   ├── views.py       # Lógica das requisições e respostas
│   ├── urls.py        # Mapeamento das rotas
│   ├── admin.py       # Configuração do painel administrativo
│── static/            # Arquivos estáticos (CSS, JS, imagens)
│   ├── img/           # Imagens utilizadas na aplicação
│── db.sqlite3         # Banco de dados SQLite
│── manage.py          # Comando principal do Django
```

## Capturas de Tela

### Tela de Login
![image](https://github.com/user-attachments/assets/ce4a7c39-9566-489a-b543-60bf2c675f89)
* Login com o Google 100% funcional

### Tela de Agendamentos
![image](https://github.com/user-attachments/assets/57d12d2d-a45b-4ff6-9089-f09fc9e84193)
* Os eventos com pelo menos uma hora de atraso são exibidos com um tom vermelho

### Tela de Criação/Edição de Evento
![image](https://github.com/user-attachments/assets/992cf1c1-45ce-45f9-a236-bd458e5f506f)
* Reaproveitei a tela de inserção de eventos para também editá-los, evitando repetição de código desnecessariamente.

## Aprendizados

Este foi meu primeiro contato com **Django**, e o desenvolvimento deste projeto foi um grande aprendizado. Em cerca de **três semanas**, explorei desde a estruturação inicial até a implementação de funcionalidades avançadas, como autenticação via **Google OAuth** e a utilização de **Bootstrap** para melhorar a interface. O projeto ainda está em aprimoramento, e pretendo continuar evoluindo suas funcionalidades e aplicando boas práticas de desenvolvimento.

## Autor

Desenvolvido por **Wendell** como parte do aprendizado em Django para o processo seletivo da **RedeBR**.

