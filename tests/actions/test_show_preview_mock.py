# mocks dos teste: test_show_preview

# primeiro caso: ao menos um elemento em "all_files"
context01 = {"all_files": ["src/__init__.py"], "all_dirs": []}
# nesse caso ela retona no termial essa string
print01 = """Found 1 files and 0 directories
First 5 files: ['src/__init__.py']\nFirst 5 directories: []\n"""


# segundo caso: ao menos um elemento em "all_dirs"
context02 = {"all_files": [], "all_dirs": ["src", "src/utils"]}
# nesse caso ela retona no termial essa string
print02 = """Found 0 files and 2 directories
First 5 files: []\nFirst 5 directories: ['src', 'src/utils']\n"""


# terceiro caso: mais de um elemento em "all_files" e "all_dirs"
context03 = {
    "all_files": [
        "./dev-requirements.txt",
        "./.gitignore",
        "./pyproject.toml",
        "./setup.cfg",
        "./README.md",
        "./requirements.txt",
    ],
    "all_dirs": [
        "./.trybe",
        "./tests",
        "./pro_filer",
        "./images",
        "./.github",
        "./.vscode",
    ],
}
# nesse caso ela retona no termial essa string
print03 = """Found 6 files and 6 directories
First 5 files: ['./dev-requirements.txt', './.gitignore', './pyproject.toml', \
'./setup.cfg', './README.md']
First 5 directories: ['./.trybe', './tests', './pro_filer', './images', \
'./.github']
"""

# quarto caso: nem um elemento em "all_files" nem em "all_dirs"
context04 = {"all_files": [], "all_dirs": []}
# nesse caso ela retona no termial essa string
print04 = """Found 0 files and 0 directories\n"""
