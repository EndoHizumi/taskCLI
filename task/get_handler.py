import dataset


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    return task_list.find()