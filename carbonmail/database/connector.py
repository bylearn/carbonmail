# Vai se conectar com o Banco de Dados
import sqlite3
import os
from carbonmail.utils import root_folder


def get_db_file():
    db_folder = os.path.join(root_folder(), "database")

    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    return os.path.join(db_folder, "contacts.db")


def connect():
    connection = None

    try:
        connection = sqlite3.connect(get_db_file())
        connection.execute("PRAGMA foreign_keys = 1")
    except sqlite3.Error as error:
        print("Ops... Deu um erro iniciando a conexão com o banco:", error)

    return connection


def close_connection(connection):
    if connection:
        connection.close()
