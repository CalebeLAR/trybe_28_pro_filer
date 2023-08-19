"""Arquivo que estudantes devem editar"""


def hof(context_all_files: [str]) -> int:
    deeper = {"path": "", "deep": 0}
    for path in context_all_files:
        splited_path = path.split("/")
        deep_path = len(splited_path)
        if deep_path > deeper["deep"]:
            deeper["deep"] = deep_path
            deeper["path"] = path

    return deeper["path"]


# show_deepest_file req01
def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = hof(context["all_files"])
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
