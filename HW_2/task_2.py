"""
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
в котором вывод разбивается на слова с удалением всех знаков пунктуации
(их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.
"""


import subprocess
from string import punctuation


def command_res(result, mode):
    if result.returncode == 0:
        output = result.stdout
        if mode == "line":
            lst = output.split("\n")
            if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in lst and 'VERSION_CODENAME=jammy' in lst:
                return True
        elif mode == "word":
            output = ''.join(char for char in output if char not in punctuation)
            words = output.split()
            if 'VERSION22041LTSJammyJellyfish' in ''.join(words) and 'VERSIONCODENAMEjammy' in ''.join(words):
                return True
    return False


result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
mode = input("Выберите режим line или word: ")

print(command_res(result, mode))