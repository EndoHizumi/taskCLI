import dataset
import datetime

def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]

    valid_argment: list = ['id', 'taskName', 'project', 'context', 'startDay', 'endDay', 'importance', 'state']
    replace_key_map: dict = {
        'startDay': 'startDt',
        'endDay': 'endDt',
        'context': 'tag',
        'importance': 'priority'
    }
    data: dict = {}
    args_dict = vars(args)

    for item in args_dict:
        if item in valid_argment and args_dict.get(item) is not None:
            key = replace_key_map.get(item, item)
            data[key] = args_dict.get(item)
    print(data)
    result_set = task_list.find(**data)

    return list(result_set)
