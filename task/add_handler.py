import dataset
from datetime import datetime


def handle(args):
    start_date = args.startDay if args.startDay else datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    length = len(task_list)
    task_list.insert(
        {
            'id': length,
            'taskName': args.taskName,
            'startDt': start_date,
            'endDt': None,
            'createAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'updateAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'project': args.project,
            'tag': args.context,
            'state': 0,
            'priority': args.importance
        }
    )
    return task_list.find_one(id=length)
