# mocks dos teste: test_show_details

# caso a chave "base_path" recebe um caminho para um arquivo existente
context01 = {}
context01[
    "base_path"
] = "tests/actions/test_show_details.py"
# nesse caso ela retona no termial essa string
print01 = """\
File name: test_show_details.py\n\
File size in bytes: 1026
File type: file
File extension: .py
Last modified date: 2023-08-25\n\
"""

# caso a chave "base_path" recebe um caminho para um diretório existente
context02 = {}
context02["base_path"] = "tests/actions"
# nesse caso ela retona no termial essa string
print02 = """\
File name: actions\n\
File size in bytes: 4096
File type: directory
File extension: [no extension]
Last modified date: 2023-08-25\n\
"""

# caso a chave "base_path" recebe um caminho para um arquivo sem extenção
context03 = {}
context03[
    "base_path"
] = "tests/actions/test_show_details"
# nesse caso ela retona no termial essa string
print03 = """\
File name: test_show_details\n\
File size in bytes: 0
File type: file
File extension: [no extension]
Last modified date: 2023-08-25\n\
"""

# caso a chave "base_path" recebe um caminho para um arquivo ou diretório
# inexistente
context04 = {}
context04[
    "base_path"
] = "tests/actions/test_show_details_mock/actions/?????.py"
# nesse caso ela retona no termial essa string
print04 = """File '?????.py' does not exist\n"""
