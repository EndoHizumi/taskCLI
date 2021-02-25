from task import get_handler as get


def handle(args):
    resultSet = list(get.handle(args))[0]
    keys = resultSet.keys()
    contents = resultSet.values()

    print()
    for key in keys:
        print(key, end=" "*8)
    print()
    print("-"*30)

    for item in contents:
        print(item, end=" "*9)
    print()
    return ""