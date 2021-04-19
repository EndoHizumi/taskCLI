import dataset


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]

    if args.all:
        result_set = task_list.find()
    elif args.done:
        result_set = task_list.find(state=[1])
    else:
        result_set = task_list.find(state=[None, 0])

    return list(result_set)
