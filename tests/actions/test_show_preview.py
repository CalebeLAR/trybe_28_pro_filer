import pytest
import tests.actions.test_show_preview_mock as mock
from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.mark.parametrize(
    "context, saida",
    [
        # primeiro caso ao menos um elemento em "all_files"
        (mock.context01, mock.print01),
        # segundo caso ao menos um elemento em "all_dirs"
        (mock.context02, mock.print02),
        # terceiro caso mais de um elemento em "all_files" e "all_dirs"
        (mock.context03, mock.print03),
        # quarto caso nem um elemento em "all_files" nem em "all_dirs"
        (mock.context04, mock.print04),
    ],
)
def test_show_preview(context, saida, capsys):
    # a função show_preview escreve quatro possiveis tipos de saida no
    # terminal de acordo com o que vem dentro das duas chaves
    # "all_file" e "all_dirs" no objeto context
    show_preview(context)
    readouterr = capsys.readouterr()
    assert readouterr.out == saida
