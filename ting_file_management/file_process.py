from ting_file_management.file_management import txt_importer
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
    if instance.__len__() == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        file_removed = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f'Arquivo {file_removed} removido com sucesso\n')


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write('Posição inválida\n')
