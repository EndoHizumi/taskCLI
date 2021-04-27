import dataset
from datetime import datetime


def handle(args):
    start_date = args.startDay if args.startDay else None
    done = 1 if args.done else 0
    end_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S") if args.done else None
    db = dataset.connect("sqlite:///taskList.sqlite")
    context = args.tag if args.tag else 'todo'
    task_list = db["taskList"]
    id_number = list(task_list.find())[-1]['id'] + 1
    task_list.insert(
        {
            'id': id_number,
            'taskName': args.taskName,
            'startDt': start_date,
            'endDt': end_date,
            'createAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'updateAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'project': args.project,
            'group': args.group,
            'tag': context,
            'state': done,
            'priority': args.importance,
        }
    )
    return task_list.find_one(id=id_number)
