from pro_filer.actions.main_actions import show_details  # NOQA
import os
from datetime import datetime


def test_show_details_of_a_file_that_exists(capsys, tmp_path):
    # caso caso receba um caminho para um arquivo existente
    tmp_dir = tmp_path / "dir"
    tmp_dir.mkdir()
    tmp_file = tmp_dir / "um_arquivo_existente.txt"
    tmp_file.write_text("texto do arquivo", encoding="utf-8")

    date = datetime.fromtimestamp(os.path.getmtime(tmp_file))
    formated_date = date.strftime("%Y-%m-%d")

    context = {}
    context["base_path"] = str(tmp_file.absolute())

    show_details(context)
    readouterr = capsys.readouterr()

    assert readouterr.out == (
        f"""\
File name: {tmp_file.name}
File size in bytes: {os.path.getsize(tmp_file)}
File type: file
File extension: {tmp_file.suffix}
Last modified date: {formated_date}\n"""
    )


def test_show_details_of_a_directory_that_exists(capsys, tmp_path):
    # caso caso receba um caminho para um diretório existente
    tmp_dir = tmp_path / "dir"
    tmp_dir.mkdir()

    context = {}
    context["base_path"] = str(tmp_dir.absolute())

    date = datetime.fromtimestamp(os.path.getmtime(tmp_dir))
    formated_date = date.strftime("%Y-%m-%d")

    show_details(context)
    readouterr = capsys.readouterr()

    assert readouterr.out == (
        f"""\
File name: {tmp_dir.name}
File size in bytes: {os.path.getsize(tmp_dir)}
File type: directory
File extension: [no extension]
Last modified date: {formated_date}\n\
"""
    )


def test_show_details_of_a_file_with_out_extension(capsys, tmp_path):
    # caso caso receba um caminho para um arquivo sem extenção
    tmp_file = tmp_path / "arquivo_sem_extenção"
    tmp_file.touch()

    date = datetime.fromtimestamp(os.path.getmtime(tmp_file))
    formated_date = date.strftime("%Y-%m-%d")

    context = {}
    context["base_path"] = str(tmp_file)

    show_details(context)
    readouterr = capsys.readouterr()

    assert readouterr.out == (
        f"""\
File name: {tmp_file.name}
File size in bytes: {os.path.getsize(tmp_file)}
File type: file
File extension: [no extension]
Last modified date: {formated_date}\n"""
    )


def test_show_details_of_a_file_or_directory_that_not_exists(capsys, tmp_path):
    # caso caso receba um caminho para um arquivo ou diretório inexistente

    context = {}
    context["base_path"] = "um_arquivo_ou_diretório_inexistente"

    show_details(context)
    readouterr = capsys.readouterr()

    assert readouterr.out == (
        "File 'um_arquivo_ou_diretório_inexistente' does not exist\n"
    )
