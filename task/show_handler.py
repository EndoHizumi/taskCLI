import texttable as ttb
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
    table = ttb.Texttable(120)  # 表型作成(大きさは以下の情報から決める）
    table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])  # 文字の配置,たぶんl(左揃え）r（右揃え）c（中央）
    table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m", "m", "m", "m"])  # 表示属性
    result_list = [list(result_set[0].keys())]
    contents = [list(item.values()) for item in result_set]
    result_list.extend(contents)
    table.add_rows(result_list)
    return table.draw()
