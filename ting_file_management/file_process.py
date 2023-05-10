from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    output = {"nome_do_arquivo": path_file,
              "qtd_linhas": len(txt_importer(path_file)),
              "linhas_do_arquivo": txt_importer(path_file)}
    instance.enqueue(output)

    return sys.stdout.write(str(output))


def remove(instance):
    if not instance or len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    path_file = instance.dequeue()['nome_do_arquivo']

    return sys.stdout.write(
        f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        return sys.stdout.write(str(instance.search(position)))
    except IndexError:
        return sys.stderr.write("Posição inválida")
