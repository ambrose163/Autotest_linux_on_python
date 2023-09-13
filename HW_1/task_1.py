"""
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess


def command_res(result):
    if result.returncode == 0:
        lst = result.stdout.split("\n")
        if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in lst and 'VERSION_CODENAME=jammy' in lst:
            return True
        else:
            return False
    else:
        return False


result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
print(command_res(result))