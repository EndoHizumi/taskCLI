import dataset
from task import find_handler as find


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    result = None

    result_set = find.handle(args)
    target_row = [item.get('id') for item in result_set]
    task_list.delete(id=target_row)

    if result_set:
        result = result_set

    return result
