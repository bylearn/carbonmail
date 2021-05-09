# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar este pacote (gerenciador)

import csv

from os.path import isfile

from carbonmail.utils import check_email, string_null_or_empty

from carbonmail.database.manager import search_list, search_contacts
from carbonmail.database.manager import create_list as db_create_list
from carbonmail.database.manager import create_contact as db_create_contact
from carbonmail.database.manager import delete_list as db_delete_list


def initialize(email_sender):
    from carbonmail.list_editor import List_Editor

    ems = List_Editor(email_sender)
    ems.enable_window()


def load_lists():
    lists = search_list()
    lists = [_list[1] for _list in lists]

    return lists


def create_list(list_name):
    if string_null_or_empty(list_name):
        return False

    db_create_list(list_name)
    return True


def create_contact(name, email, list_name):
    if (
        string_null_or_empty(name)
        or string_null_or_empty(email)
        or not check_email(email)
    ):
        return False

    lists = search_list()

    list_id = 0
    for _list in lists:
        if _list[1] == list_name:
            list_id = _list[0]
            break

    db_create_contact(name, email, list_id)
    return True


def import_contacts(csv_path, list_name):

    if not isfile(csv_path):
        return -1

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024))
        csv_file.seek(0)

        reader = csv.DictReader(csv_file, dialect=dialect)

        if not "name" in reader.fieldnames or not "email" in reader.fieldnames:
            return 0

        for row in reader:
            create_contact(row["name"], row["email"], list_name)

        return 1


def delete_list(list_name):
    db_delete_list()


def get_list_contacts(list_name):
    return search_contacts(list_name)


def update_lists(window, select_list=None):
    lists = load_lists()

    if select_list:
        select_index = lists.index(select_list)
    else:
        select_index = 0

    window["-Lists-"].Update(values=lists, value=lists[select_index])
