from task import get_handler as get
from pprint import pprint

def handle(args):
    resultSet = list(get.handle(args))
    keys = resultSet[0].keys()

    for key in keys:
        print(key, end=" "*8)
    print()
    print("-"*30)

    for item in resultSet:
        pprint((list(item.values())))
    print()
    return ""