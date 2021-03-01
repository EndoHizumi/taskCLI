import dataset
from datetime import datetime


def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    
    task_list.insert(
        {
            'id': length,
            'taskName': args.taskName,
            'startDt': start_date,
            'endDt': end_date,
            'updateAt': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'project': args.project,
            'tag': args.context,
            'state': 0,
            'priority': args.importance
        }
    )
    return task_list.find_one(id=length)
