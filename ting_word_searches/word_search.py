def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        linhas_arquivo = instance.search(i)["linhas_do_arquivo"]
        nome_arquivo = instance.search(i)["nome_do_arquivo"]
        ocorrencias = [
            {"linha": j + 1}
            for j, linha in enumerate(linhas_arquivo)
            if word.lower() in linha.lower()
        ]

        if ocorrencias:
            if any(o["linha"] for o in ocorrencias):
                result.append(
                    {
                        "palavra": word,
                        "arquivo": nome_arquivo,
                        "ocorrencias": ocorrencias,
                    }
                )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
