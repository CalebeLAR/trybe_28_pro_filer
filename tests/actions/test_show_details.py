from pro_filer.actions.main_actions import show_details  # NOQA
import tests.actions.test_show_details_mock as mock
import pytest


@pytest.mark.parametrize(
    "context, saida",
    [
        # a chave "base_path" recebe um caminho para um arquivo existente
        (mock.context01, mock.print01),
        # a chave "base_path" recebe um caminho para um diretório existente
        (mock.context02, mock.print02),
        # a chave "base_path" recebe um caminho para um arquivo sem extenção
        (mock.context03, mock.print03),
        # a chave "base_path" recebe um caminho para um arquivo ou diretório
        # inexistente
        (mock.context04, mock.print04),
    ],
)
def test_show_details_of_a_file_that_exists(context, saida, capsys, tmp_path):
    # a função show_details escreve quatro possiveis tipos de saida no
    # terminal de acordo com o que vem dentro da chave "base_path"
    # no objeto context
    show_details(context)
    readouterr = capsys.readouterr()
    assert readouterr.out == saida
