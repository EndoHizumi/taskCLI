import dataset


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]

    valid_argment: list = ['id', 'taskName', 'project', 'context', 'startDay', 'endDay', 'importance', 'state']
    replace_key_map: dict = {
        'id': ['=', 'id'],
        'taskName': ['=', 'taskName'],
        'project': ['=', 'project'],
        'context': ['=', 'tag'],
        'startDay': ['like', 'startDt'],
        'endDay': ['like', 'endDt'],
        'importance': ['=', 'priority'],
        'state': ['=', 'state']
    }
    data: dict = {}
    args_dict = vars(args)

    if args_dict['startDay']:
        args_dict['startDay'] = f"{args_dict['startDay'].date().strftime('%Y/%m/%d')}%"

    if args_dict['endDay']:
        args_dict['endDay'] = f"{args_dict['endDay'].date().strftime('%Y/%m/%d')}%"

    for item in args_dict:
        if item in valid_argment and args_dict.get(item) is not None:
            key = replace_key_map.get(item)[1]
            data[key] = {replace_key_map.get(item)[0]: args_dict.get(item)}

    print(data)
    result_set = task_list.find(**data)

    return list(result_set)
