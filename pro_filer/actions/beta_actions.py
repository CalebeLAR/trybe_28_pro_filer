"""Arquivo que estudantes devem editar"""


def get_deepest_file(context_all_files: [str]) -> int:
    # Inicializa um dicionário para armazenar o caminho mais profundo e sua
    # profundidade
    deeper = {"path": "", "deep": 0}

    # Itera por cada caminho de arquivo na lista de caminhos de arquivos
    for path in context_all_files:
        # Divide o caminho em partes separadas por "/"
        splited_path = path.split("/")

        # Calcula a profundidade do caminho dividido contando as partes
        deep_path = len(splited_path)

        # Verifica se a profundidade do caminho atual é maior do que a
        # profundidade armazenada
        if deep_path > deeper["deep"]:
            # Atualiza o dicionário com a nova profundidade e o novo caminho
            # mais profundo
            deeper["deep"] = deep_path
            deeper["path"] = path

    # Retorna o caminho mais profundo encontrado
    return deeper["path"]


# show_deepest_file req01
def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = get_deepest_file(context["all_files"])
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name = file_name.lower()
            search_term = search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
