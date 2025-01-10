#📚 Mini Sistema de Blog com Django
Este é um projeto de um pequeno sistema de blog, neste caso foi utilizado para desenvolver um blog sobre noticias do mundo automotivo 

---
# Técnologias utilzadas
- Python 3.10
- Django 5.1
- SQLite3
- HTML5
- CSS3
- Bootstrap 5
- **Pillow** (para trabalhar com imagens)

---

## 🚀 **Funcionalidades**

- 📄 Listagem de posts em ordem cronologia (do antigo ao mais novo)
- ✏️ Criação de novos posts
- 🖼️ Upload de imagens para posts
- 📝 Edição de posts existentes
- 🗑️ Exclusão de posts
- 💬 Formulário de contato

---

## ⚙️ **Pré-requisitos**

- Python 3.x instalado
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

---

## 📦 **Como Instalar o Projeto**

1️⃣ **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2️⃣ Crie um ambiente virtual e ative-o:

```
# No Windows
python -m venv env
env\Scripts\activate

# No Linux/macOS
python3 -m venv env
source env/bin/activate
```

3️⃣ Instale as dependências:

```
pip install -r requirements.txt
```

4️⃣ Faça as migrações do banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

5️⃣ Execute o servidor de desenvolvimento:

```
python manage.py runserver
```

---

🖥️ Como Usar o Projeto
- Acesse o endereço http://localhost:8000/blog/ no seu navegador.
- Utilize a interface para criar, editar, visualizar e excluir posts.
- Faça upload de imagens para os posts.
- Utilize o formulário de contato.

---

📝 Comandos Úteis
Comando	Descrição
- python manage.py runserver	Inicia o servidor de desenvolvimento.
- python manage.py makemigrations	Cria as migrações do banco de dados.
- python manage.py migrate	Aplica as migrações no banco de dados.
- python manage.py createsuperuser	Cria um usuário administrador.
  
---

📚 Decisões Técnicas
- A decisão de utilizar Python e Django foi tomada porque eu já possuía conhecimento básico em Python, o que facilitou o desenvolvimento.
- O SQLite3 foi escolhido como banco de dados por ser simples de configurar e integrado ao Django, acelerando o desenvolvimento.
- O uso do Bootstrap 5 foi uma escolha estratégica para facilitar a estilização da interface, mesmo com pouca experiência em front-end.
- A biblioteca Pillow foi utilizada para adicionar o recurso de upload de imagens, o que foi fundamental para permitir que os posts tenham imagens ilustrativas.

---

📚 O que Foi Aprendido Durante o Desenvolvimento
  - Este foi meu primeiro projeto solo em desenvolvimento full-stack onde tive algumas dificuldades por serem muitas coisas novas porem com esforço consegui concluir-lo.
  
🧱 1. Estrutura de Projetos Django
- Criar projetos e apps no Django.
- Entender a importância dos arquivos models.py, views.py, urls.py e forms.py.
📄 2. Templates HTML e CSS
- Trabalhar com templates HTML para gerar páginas dinâmicas.
- Configurar e servir arquivos estáticos (CSS) no Django.
🗄️ 3. Banco de Dados e Migrações
- Criar models para definir tabelas no banco de dados.
- Utilizar migrations para criar e atualizar tabelas.
📤 4. Upload de Imagens
- Configurar o campo ImageField para permitir o upload de imagens.
- Utilizar a biblioteca Pillow para manipulação de imagens.
🔄 5. Formulários no Django
- Criar forms com forms.Form e forms.ModelForm.
- Processar dados de formulários e validar entradas do usuário.
🔧 6. URLs Dinâmicas e Redirecionamentos
- Utilizar parâmetros dinâmicos nas URLs (como IDs de posts).
- Implementar redirecionamentos após submissões de formulários.
📦 7. Trabalhar com Ambiente Virtual e Dependências
- Criar e ativar um ambiente virtual para o projeto.
- Gerar e utilizar o arquivo requirements.txt para instalar dependências.

---

📜 Licença
- Use como quiser, Sinta-se livre para utilizar e modificar conforme necessário. 😊


---


👤 Autor
Pedro H.P Carvalho
🌐 LinkedIn (https://www.linkedin.com/in/pedro-henrique-carvalho-71b334208/)
🌐 GitHub = (https://github.com/PedroHPCarvalho)




