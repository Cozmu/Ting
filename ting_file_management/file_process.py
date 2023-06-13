from ting_file_management.file_management import txt_importer
from queue import Queue
import sys

def process(path_file, instance):
    list_file = txt_importer(path_file)
    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_file),
        "linhas_do_arquivo": list_file 
    }

    for element in instance.get_list():
        if element["nome_do_arquivo"] == dict_file["nome_do_arquivo"]:
            return None
    
    instance.enqueue(dict_file)
    sys.stdout.write(str(dict_file))

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
