import argparse
import prettytable
from datetime import datetime

from task import (add_handler, done_handler, remove_handler, show_handler, start_handler, update_handler, find_handler, state_handler)


def validate_date(arg_date):
    try:
        return datetime.now().strptime(arg_date, "%Y/%m/%d")
    except ValueError:
        msg = f"Not a valid date: '{arg_date}'."
        raise argparse.ArgumentTypeError(msg)


def draw_table(result_set):

    header = ['id', 'taskName', 'state', 'startDt', 'endDt',
              'createAt', 'updateAt', 'project', 'group', 'priority', 'tag']
    contents = []

    if result_set:
        if type(result_set) is list:
            header = list(result_set[0].keys())
            contents = [list(item.values()) for item in result_set]
        else:
            header = list(result_set.keys())
            contents = [[result_set[item] for item in result_set]]

    table = prettytable.PrettyTable(header)
    for item in contents:
        table.add_row(item)
    return table


def get_arg_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    add_parser = sub_parser.add_parser(
        'add', help='Insert task to TaskList. If priority is omitted, priority medium is set.')
    add_parser.add_argument('-t', '--taskName', type=str, required=True)
    add_parser.add_argument('-p', '--project', type=str, default='')
    add_parser.add_argument('-c', '--context', type=str, default='')
    add_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    add_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    add_parser.add_argument('-i', '--importance', type=str, default='C', choices=['A', 'B', 'C', 'D', 'E'])
    add_parser.add_argument('-d', '--done', action='store_true')
    add_parser.add_argument('-g', '--group', type=str, default='')
    add_parser.set_defaults(func=add_handler.handle)

    done_parser = sub_parser.add_parser('done', help='Done to task')
    done_parser.add_argument('id')
    done_parser.set_defaults(func=done_handler.handle)

    show_parser = sub_parser.add_parser('show', help='show taskList')
    show_parser.add_argument("-a", "--all", action='store_true')
    show_parser.add_argument("-d", "--doneOnly", action='store_true')
    show_parser.add_argument('-t', '--taskName', type=str)
    show_parser.add_argument('-p', '--project', type=str)
    show_parser.add_argument('-c', '--context', type=str)
    show_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    show_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    show_parser.add_argument('-i', '--importance', type=str, choices=['A', 'B', 'C', 'D', 'E'])
    show_parser.set_defaults(func=show_handler.handle)

    update_parser = sub_parser.add_parser('update', help='Update the task. The target is specified the id and option.')
    update_parser.add_argument('id')
    update_parser.add_argument('-t', '--taskName', type=str)
    update_parser.add_argument('-p', '--project', type=str)
    update_parser.add_argument('-c', '--context', type=str)
    update_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    update_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    update_parser.add_argument('-i', '--importance', type=str, choices=['A', 'B', 'C', 'D', 'E'])
    update_parser.set_defaults(func=update_handler.handle)

    start_parser = sub_parser.add_parser('start')
    start_parser.add_argument('id')
    start_parser.set_defaults(func=start_handler.handle)

    remove_parser = sub_parser.add_parser('remove', help='remove the specified task. The target can multiple specify from search result.')
    remove_parser.add_argument('id', nargs='?')
    remove_parser.add_argument('-t', '--taskName', type=str)
    remove_parser.add_argument('-p', '--project', type=str)
    remove_parser.add_argument('-c', '--context', type=str)
    remove_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    remove_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    remove_parser.add_argument('-i', '--importance', type=str, choices=['A', 'B', 'C', 'D', 'E'])
    remove_parser.set_defaults(func=remove_handler.handle)

    find_parser = sub_parser.add_parser('find', help='display only match to the conditions.')
    find_parser.add_argument('-t', '--taskName', type=str)
    find_parser.add_argument('-p', '--project', type=str)
    find_parser.add_argument('-c', '--context', type=str)
    find_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    find_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    find_parser.add_argument('-i', '--importance', type=str, choices=['A', 'B', 'C', 'D', 'E'])
    find_parser.set_defaults(func=find_handler.handle)
    
    state_parser = sub_parser.add_parser('state', help='')
    state_parser.add_argument('-t', '--taskName', type=str)
    state_parser.add_argument('-p', '--project', type=str)
    state_parser.add_argument('-c', '--context', type=str)
    state_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    state_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    state_parser.add_argument('-i', '--importance', type=str, choices=['A', 'B', 'C', 'D', 'E'])
    state_parser.set_defaults(func=find_handler.handle)

    return parser


if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    print(draw_table(args.func(args)))
