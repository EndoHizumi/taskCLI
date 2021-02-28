import argparse
from task import add_handler
from task import done_handler
from task import show_handler
from datetime import datetime


def validate_date(arg_date):
    try:
        return datetime.now().strptime(arg_date, "%Y/%m/%d")
    except ValueError:
        msg = f"Not a valid date: '{arg_date}'."
        raise argparse.ArgumentTypeError(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    add_parser = sub_parser.add_parser('add', help='Insert task to TaskList. If priority is omitted, priority medium is set.')
    add_parser.add_argument('-t', '--taskName', type=str, required=True)
    add_parser.add_argument('-p', '--project', type=str, default='')
    add_parser.add_argument('-c', '--context', type=str, default='')
    add_parser.add_argument('-s', '--startDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    add_parser.add_argument('-e', '--endDay', type=validate_date, help='date input format %%Y/%%m/%%d %%H:%%M:%%S')
    add_parser.add_argument('-i', '--importance', type=str, default='C', choices=['A', 'B', 'C', 'D', 'E'])
    add_parser.set_defaults(func=add_handler.handle)

    done_parser = sub_parser.add_parser('done', help='Done to task')
    done_parser.add_argument('id')
    done_parser.set_defaults(func=done_handler.handle)

    show_parser = sub_parser.add_parser('show', help='show taskList')
    show_parser.add_argument("-a", "--all", action='store_true')
    show_parser.add_argument("-d", "--done", action='store_true')
    show_parser.set_defaults(func=show_handler.handle)
    show_parser.add_argument("filter", nargs="?", default='')

    args = parser.parse_args()
    print(args.func(args))
