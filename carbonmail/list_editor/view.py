# É onde fica o código para a Interface Gráfica
# Tudo que existir de VISUAL vai ficar aqui
# É principalmente aqui que usaremos o PySimpleGUI

from carbonmail.list_editor.manager import load_lists
import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

lista = load_lists()


def get_layout():

    frame_list = [
        inner_element_space(600),
        [
            sg.Text("Selecione a lista:"),
            sg.Combo(lista, default_value=lista[0], key="-Lists-"),
        ],
        [
            sg.Text("Criar uma lista:"),
            sg.In(key="-ListName-"),
            sg.Button("Criar", key="-Create-", size=(10, 1)),
        ],
        [
            sg.Button(
                "Deletar a Lista",
                key="-Delete-",
                size=(15, 1),
                pad=(5, (7, 7)),
            ),
            sg.Button(
                "Mostrar Contatos",
                key="-ShowContacts-",
                size=(15, 1),
                pad=(5, (7, 7)),
            ),
        ],
        inner_element_space(600),
    ]

    frame_import = [
        inner_element_space(600),
        [
            sg.Text(
                "Selecione o arquivo (CSV):",
                tooltip="Cabeçalhos: name e email",
            ),
            sg.In(key="-CSV-"),
            sg.FileBrowse(
                "Selecionar",
                file_types=(("CSV", "*.csv"),),
                tooltip="Cabeçalhos: name e email",
            ),
        ],
        [
            sg.Button(
                "Importar Contatos",
                key="-Import-",
                size=(15, 1),
                pad=(0, (7, 7)),
            ),
        ],
        inner_element_space(600),
    ]

    frame_add = [
        inner_element_space(600),
        [sg.Text("Insira o nome:"), sg.In(key="-Name-")],
        [sg.Text("Insira o email:"), sg.In(key="-Email-")],
        [
            sg.Button(
                "Adicionar Contato",
                key="-Add-",
                size=(15, 1),
                pad=(0, (7, 7)),
            ),
        ],
        inner_element_space(600),
    ]

    layout = [
        [
            sg.Frame(
                "Configurações da Lista",
                frame_list,
                element_justification="c",
            )
        ],
        [
            sg.Frame(
                "Importar Contatos",
                frame_import,
                element_justification="c",
            )
        ],
        [
            sg.Frame(
                "Adicionar Contato",
                frame_add,
                element_justification="c",
            )
        ],
        [
            sg.Button(
                "Voltar",
                key="-Back-",
                size=(15, 1),
                pad=(0, (7, 7)),
            )
        ],
        inner_element_space(600),
    ]

    return layout


def get_window():
    # Temas: https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg
    sg.theme("DarkBlue14")
    return sg.Window(
        "Editor de Lista",
        get_layout(),
        element_justification="c",
    )
