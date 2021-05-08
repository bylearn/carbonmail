# É onde fica o código para a Interface Gráfica
# Tudo que existir de VISUAL vai ficar aqui
# É principalmente aqui que usaremos o PySimpleGUI
import PySimpleGUI as sg


# Window => Janela
# Layout => O que vai mostrar na janela
#        =>=> Lista de Listas
#             Cada sublista é uma "Linha" da Janela
#             Cada elemento é um componente visual

lista = ["Administradores", "Alunos"]


def get_layout():
    layout = [
        [
            sg.Text("Selecione o Seu Código"),
            sg.In(),
            sg.FileBrowse("Selecione", file_types=(("Códigos Python", "*.py"),)),
        ],
        [
            sg.Text("Selecione a lista de destinatários"),
            sg.Combo(lista, default_value=lista[1]),
        ],
        [
            sg.Text("Insira o Título: "),
            sg.In(key="-Title-"),
        ],
        [
            sg.Text("Insira o Conteudo do E-mail: "),
            sg.MLine(key="-Content-"),
        ],
        [
            sg.Button("Enviar", key="-Send-"),
            sg.Button("Gerenciar Listas", key="-ListEditor-"),
        ],
    ]

    return layout


def get_window():
    return sg.Window("Teste de Janela", get_layout())
