def find_occurrences(lines_list_file, word):
    contador = 1
    result = []
    for line in lines_list_file:
        if word.lower() in line.lower():
            result.append({"linha": contador})

        contador += 1

    return result


def exists_word(word, instance):
    result = []
    for dict_file in instance.get_list():
        occurrences = find_occurrences(dict_file["linhas_do_arquivo"], word)
        if len(occurrences) != 0:
            dict_result = {
                "palavra": word,
                "arquivo": dict_file["nome_do_arquivo"],
                "ocorrencias": occurrences
            }
            result.append(dict_result)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
