# additional functions for the taskstring dict
# version: alpha1.4
# authors: Niklas Munkes

def void(input: str) -> str:
    return input


def tprint(index: int) -> None:
    print("tokenizing paragraph " + str(index) + "...")


def nprint(index: int) -> None:
    print("normalizing paragraph " + str(index) + "...")


def wprint(index: int) -> None:
    print("removing stop words from paragraph " + str(index) + "...")


def sprint(index: int, stemmer: str) -> None:
    print("stemming paragraph " + str(index) + " with " + stemmer + " stemmer" + "...")


def ts_porter() -> str:
    return "porter"


def ts_lancaster() -> str:
    return "lancaster"


def ts_sulyvahn() -> str:
    return "sulyvahn"