from task import get_handler as get
from pprint import pprint
import texttable as ttb


def handle(args):
    result_set = list(get.handle(args))
    # table例01(3*3)
    table = ttb.Texttable(120)  # 表型作成(大きさは以下の情報から決める）
    table.set_cols_align(["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])  # 文字の配置,たぶんl(左揃え）r（右揃え）c（中央）
    table.set_cols_valign(["m", "m", "m", "m", "m", "m", "m", "m", "m", "m"])  # 表示属性
    result_list = [list(result_set[0].keys())]
    contents = [list(item.values()) for item in result_set]
    result_list.extend(contents)
    table.add_rows(result_list)
    print(table.draw() + "\n")  # 表示
    return ""
