# Carbonmain

Aplicação que utiliza a API não oficial do carbon.now.sh (carbonara) para gerar imagens através de códigos existentes de Python e enviar para uma lista de contatos.

O código foi feito apenas para fins educacionais, ensinando nossos alunos do curso de Python como criar uma aplicação real :)

Todas as funcionalidades abaixo são para estudo, afim de mostrar partes diversas que aprendemos no pacote Python Faixa Preta

## Funcionalidades

- Criação de listas
- Adição de contatos
- Importação de contatos em lote
- Envio de e-mail em lote
- Geração de imagem através de código
- Manipulação de planilhas excel
- Automação de processos
- Integração com o sistema operacional
- Utilização de API
- Utilização de banco de dados
- Criação de módulos do Python
- Uso de pacotes externos
- Boas práticas no Python
- Elaboração de interfaces gráficas
- Prototipação de projetos
- Criação de executáveis a partir do Python
- Programação Orientada a Objetos

## Configuração

É preciso criar um arquivo chamado '**.env**' _(nome vazio e extensão env)_ na pasta raiz do projeto e inserir o seguinte conteúdo:

    SMTP_USER=seu@email.com
    SMTP_PASSWORD=suasenha
    SMTP_SERVER=smtp.servidor.email
    SMTP_PORT=porta_do_email

Exemplo:

    SMTP_USER=email@gmail.com
    SMTP_PASSWORD=senhalegal
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587

# Executando

Navegue até a pasta raiz.

Instale as dependências com:

pip install -r requirements.txt

# Criando um executável

Use o seguinte comando:

```bash
pyinstaller -wF --clean .\carbonmail\__main__.py -i carbon.ico
```
