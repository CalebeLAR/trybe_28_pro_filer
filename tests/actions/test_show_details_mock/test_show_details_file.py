# from pro_filer.actions.main_actions import show_details  # NOQA
# import os
# from datetime import datetime


# def test_show_details_of_a_file_that_exists(capsys, tmp_path):
#     # caso caso receba um caminho para um arquivo existente
#     tmp_path_dir = tmp_path / "tmp_path_dir"
#     tmp_path_dir.mkdir()
#     tmp_path_file = tmp_path_dir / "um_arquivo_existente.txt"
#     tmp_path_file.write_text("texto do arquivo", encoding="utf-8")

#     file_type = ""
#     if tmp_path_file.is_file():
#         file_type = "file"
#     if tmp_path_file.is_dir():
#         file_type = "directory"

#     date = datetime.fromtimestamp(os.path.getmtime(tmp_path_file))
#     form = date.strftime("%Y-%m-%d")

#     context = {}
#     context["base_path"] = str(tmp_path_file.absolute())

#     show_details(context)
#     readouterr = capsys.readouterr()

#     assert readouterr.out == (
#         f"""\
# File name: {tmp_path_file.name}
# File size in bytes: {os.path.getsize(tmp_path_file)}
# File type: {file_type}
# File extension: {tmp_path_file.suffix}
# Last modified date: {form}\n"""
#     )
