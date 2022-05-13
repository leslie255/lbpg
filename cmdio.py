from datetime import datetime

def __printDate() -> None:
    print("\x1b[1;36m", end="")
    print("[" + str(datetime.now()) + "] ", end="")
    print("\x1b[0m", end="")

def log(prompt: str, end='\n') -> None:
    __printDate()
    print(prompt + end, end="")

def logClean(prompt: str, end='\n') -> None:
    print(prompt + end, end="")

def logErr(prompt: str, end='\n') -> None:
    __printDate()
    print("\x1b[1;31m", end="")
    print(prompt + end, end="")
    print("\x1b[0m", end="")

def logErrClean(prompt: str, end='\n') -> None:
    print("\x1b[1;31m", end="")
    print(prompt + end, end="")
    print("\x1b[0m", end="")

def askYesOrNo(prompt: str, default=True) -> bool:
    log(prompt)
    answer = input().lower()
    if answer == "yes" or answer == "y":
        return True
    elif answer == "no" or answer == "n":
        return False
    else:
        return default

