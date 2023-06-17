import os
import re

# replace de cada linha do arquivo, utilize uma regex

# Folder Path
path = "C:\\work\\Dev"
path_new = "C:\\work\\Dev"
os.chdir(path)


def read_text_file(file_path):
    replacement = ''
    data = ''
    document = ''
    regex = r' \d\d\d\d-\d\d-\d\d'  # Escolha tua regex
    with open(file_path, 'r') as f:
        for line in f:
            data = re.search(regex, line, re.IGNORECASE).group(0)
            replacement = re.sub(regex, '', line)
            replacement = replacement.rstrip() + data
            document = document + replacement + "\n"

    # print(document)
    with open(file_path, 'w+') as f:
        f.write(document)


for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)
