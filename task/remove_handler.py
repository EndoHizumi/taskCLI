import dataset


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    target_row = task_list.find_one(id=args.id)
    task_list.delete(id=args.id)
    return target_row
