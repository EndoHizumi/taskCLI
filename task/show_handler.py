import dataset
from task import find_handler as find


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]

    args_dict = vars(args)
    args_dict.pop('func')
    is_empty = not any(args_dict.values())

    if is_empty:
        result_set = task_list.find(state=[None, 0])
    else:
        if args.all:
            result_set = task_list.find()
        elif args.doneOnly:
            result_set = [item for item in find.handle(args) if item['state'] == 1]
        else:
            result_set = [item for item in find.handle(args) if item['state'] == 0]
    result: list = []
    for item in result_set:
        del item['createAt'], item['updateAt']
        result.append(item)

    return list(result)
