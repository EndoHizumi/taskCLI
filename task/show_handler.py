import dataset
from task import find_handler as find

def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]

    args_dict = vars(args)
    args_dict.pop('func')
    is_empty = not any(args_dict.values())

    if args.all:
        result_set = task_list.find()
    elif args.doneOnly:
        result_set = task_list.find(state=[1])
    elif is_empty:
        result_set = task_list.find(state=[None, 0])
    else:
        result_set = find.handle(args)

    return list(result_set)
