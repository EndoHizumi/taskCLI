import dataset
from datetime import datetime


def handle(args):
    start_date = args.startDay if args.startDay else None
    done = 1 if args.done else 0
    end_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S") if args.done else None
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    length = len(task_list)
    task_list.insert(
        {
            'id': length,
            'taskName': args.taskName,
            'startDt': start_date,
            'endDt': end_date,
            'createAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'updateAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'project': args.project,
            'group': args.group,
            'tag': args.context,
            'state': done,
            'priority': args.importance,
        }
    )
    return task_list.find_one(id=length)
