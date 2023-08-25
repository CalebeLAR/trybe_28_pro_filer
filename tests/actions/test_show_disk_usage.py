from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage(capsys, tmp_path):
    # A função show_disk_usage imprime na saída padrão (stdout) o espaço
    # total ocupado por todos os arquivos dentro do diretório informado.

    tmp_dir01 = tmp_path / "dir"
    tmp_dir02 = tmp_path / "dir02"
    tmp_dir01.mkdir()
    tmp_dir02.mkdir()
    tmp_file01 = tmp_dir01 / "arquivo01.py"
    tmp_file01.write_text("uma string bem grande", encoding="utf-8")
    tmp_file02 = tmp_dir01 / "arquivo02.py"
    tmp_file02.write_text("uma string", encoding="utf-8")

    context = {}
    context["all_files"] = [str(tmp_file01), str(tmp_file02)]
    root_dir = str(tmp_dir01).split('/')[2]
    char81 = f"""\
'/tmp/{root_dir}/pytes...w_disk_usage0/dir/arquivo01.py':        21 (67%)
'/tmp/{root_dir}/pytes...w_disk_usage0/dir/arquivo02.py':        10 (32%)
Total size: 31
"""
    show_disk_usage(context)
    readouterr = capsys.readouterr()
    assert readouterr.out == char81

    context = {}
    context["all_files"] = []
    out = "Total size: 0\n"
    show_disk_usage(context)
    readouterr = capsys.readouterr()
    assert readouterr.out == out
