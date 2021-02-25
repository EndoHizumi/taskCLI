import dataset


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    task_list.update({'id': args.id, 'state': 1}, ['id'])
    return task_list.find_one(id=args.id)
