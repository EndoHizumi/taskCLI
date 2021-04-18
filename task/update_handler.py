import dataset
from datetime import datetime


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
    data: dict = dict(id=args.id, updateAt=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    args_dict = vars(args)

    for item in args_dict:
        if item in valid_argment and args_dict.get(item) is not None:
            key = replace_key_map.get(item, item)
            data[key] = args_dict.get(item)

    task_list.update(data, ['id'])
    return task_list.find_one(id=args.id)
