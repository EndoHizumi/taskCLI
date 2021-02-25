import argparse
from task import add_handler
from task import done_handler
from task import show_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    find_parser = sub_parser.add_parser('add', help='Insert task to TaskList. If priority is omitted, priority medium is set.')
    find_parser.add_argument('-t', '--taskName')
    find_parser.set_defaults(func=add_handler.handle)

    emboss_parser = sub_parser.add_parser('done', help='Done to task')
    emboss_parser.add_argument('-i', '--id', type=str)
    emboss_parser.set_defaults(func=done_handler.handle)

    status_parser = sub_parser.add_parser('show', help='show taskList')
    status_parser.set_defaults(func=show_handler.handle)

    args = parser.parse_args()
    print(args.func(args))
