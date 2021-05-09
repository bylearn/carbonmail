# Arquivo principal (inicial) a ser executado.
# Quando iniciamos o projeto (carbonmail) ele é o primeiro ao Python executar.
# Nós usamos para ser o Ponto de Entrada da Aplicação
from carbonmail.email_sender.manager import initialize as init_sender
from carbonmail.database.initializer import initialize as init_db

init_db()
init_sender()
