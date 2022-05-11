openedFiles = []

def fopen(path: str, flags: str):
    global openedFiles
    file = open(path, flags)
    openedFiles.append(file)
    return file

def closeAllOpenedFiles() -> None:
    global openedFiles
    for file in openedFiles:
        file.close()

def getText(path: str) -> str:
    content = ""
    for line in open(path, "r").readlines():
        content += line
    return content

