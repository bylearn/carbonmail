# Arquivo usado para transformar a Pasta em Pacote
# Ele é sempre executado ao importar este pacote

import PySimpleGUI as sg


def inner_element_space(width=100):
    return [sg.Text(" " * width, font=("Arial", 1))]
