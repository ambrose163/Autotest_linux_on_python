

import subprocess
from lib_checkout import checkout

folder_tst = "/home/user/tst"
folder_out = "/home/user/out"
folder_ext = "/home/user/folder_1"
file_in_ext = "/home/user/ext/test.txt"

def test_step1():
    """проверка команды a (архивация)"""
    assert checkout(f"cd {folder_out}; 7z a ../out/arx2 test_file.txt", "Everithing is ok"), "test 1 FAIL"

def test_step2():
    """проверка команды e (распаковка)"""
    assert checkout(f"cd {folder_out}; 7z e arx2.7z -o{folder_ext}", "Everithing is ok"), "test 2 FAIL "

def test_step1_1():
    """при архивации дополнительно проверяется создание файла"""
    res_1 = checkout(f"cd {folder_out}; 7z a ../out/arx2 test_file.txt", "Everithing is ok")
    res_2 = checkout(f"ls {folder_out};", "arx2.7z")
    assert res_1 and res_2, "test 1_1 FAIL"

def test_step2_1():
    """при распаковке проверяется создание файла"""
    res_1 = checkout(f"cd {folder_out}; 7z e arx2.7z -o{folder_ext}", "Everithing is ok")
    res_2 = checkout(f"ls {folder_out};", "test_file.txt")
    assert res_1 and res_2, "test 2_1 FAIL"

def test_step3():
    """проверка команды t (для проверки целостности архива)"""
    assert checkout(f"cd {folder_out}; 7z t arx2.7z", "Everithing is ok"), "test 3 FAIL"

def test_step4():
    """проверка команды u (обновление архива)"""
    assert checkout(f"cd {folder_out}; 7z u arx2.7z", "Everithing is ok"), "test 4 FAIL "

def test_step5():
    """проверка команды d (удаление из архива)"""
    assert checkout(f"cd {folder_out}; 7z d arx2.7z", "Everithing is ok"), "test 5 FAIL "

def test_step6():
    """проверка команды l (вывода списка файлов)"""
    assert checkout(f"cd {folder_out}; 7z l arx2.7z {folder_ext}", f"{file_in_ext}")

def test_step7():
    """проверка команды x (разархивирования с путями)"""
    res_1 = checkout(f"cd {folder_out}; 7z x arx2.7z -o{folder_ext}", "Everithing is ok")
    res_2 = checkout(f"ls {folder_ext};", f"{file_in_ext}")
    assert res_1 and res_2, "test 7 FAIL"


def test_step8():
    """проверка команды h (расчета хеша)"""
    res1 = checkout(f"cd {folder_tst}; 7z h test1.txt", "Everything is Ok")
    hash_value = subprocess.run(f"cd {folder_tst}; crc32 test1.txt", shell=True, stdout=subprocess.PIPE, encoding="utf-8").stdout.strip().upper()
    res2 = checkout(f"cd {folder_tst}; 7z h test1.txt", hash_value)
    assert res1 and res2, "test 8 FAIL"

# Запуск тестов из командной строки: cd Home_work_2/
# pytest test_task_1.py
# pytest test_task_1.py -v

# Аналог команды запуска: python3 -m pytest test_task_1.py -v
# Проверка наличия тестов: python3 -m pytest test_task_1.py -v --collect-only