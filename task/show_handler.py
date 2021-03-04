import prettytable
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

    return draw_table(list(result_set))


def draw_table(result_set):
    header = ['id', 'taskName', 'state', 'startDt', 'endDt', 'createAt', 'updateAt', 'project', 'tag', 'priority']
    contents = [list(item.values()) for item in result_set]
    table = prettytable.PrettyTable(header)
    for item in contents:
        table.add_row(item)
    return table
