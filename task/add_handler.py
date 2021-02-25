import dataset


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    length = len(task_list)
    task_list.insert({'id': length, 'taskName': args.taskName})
    return task_list.find_one(id=length)
