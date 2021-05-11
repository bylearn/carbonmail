# Arquivo usado para transformar a Pasta em Pacote
# Ele é sempre executado ao importar este pacote
from carbonmail.email_sender.manager import validate_email_sending
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import view
from carbonmail.list_editor.manager import initialize as init_list_editor
from carbonmail.list_editor.manager import update_lists


class Email_Sender:
    def __init__(self):
        self.window = None

    def instantiate(self):
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if values is not None:
                self.list = values["-Lists-"]

            if event == WIN_CLOSED:
                self.close_window()
                break

            elif event == "-Send-":
                title = values["-Title-"]
                content = values["-Content-"]
                code = values["-Code-"]

                status_code = validate_email_sending(
                    self.window, title, content, code, self.list
                )

                if status_code == 0:
                    sg.popup("Lista sem contatos válidos", title="Erro")
                elif status_code == -1:
                    sg.popup("Título ou Conteúdo inválido", title="Erro")
                elif status_code == -2:
                    sg.popup("Código (arquivo) não encontrado", title="Erro")
                else:
                    sg.popup(
                        "Os e-mails estão sendo enviados. Por favor, aguarde!",
                        title="Sucesso",
                        non_blocking=True,
                    )

            elif event == "-ListEditor-":
                self.hide_window()
                init_list_editor(self)

            elif event == "-Sent-":
                sg.popup("Todos os e-mails foram enviados!", title="Sucesso")

    def close_window(self):
        if self.window is not None:
            self.window.Close()
        self.window = None

    def hide_window(self):
        if self.window is not None:
            self.window.Hide()

    def unhide_window(self):
        update_lists(self.window, self.list)
        if self.window is not None:
            self.window.UnHide()
