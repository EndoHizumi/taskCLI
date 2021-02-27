import dataset
from datetime import datetime


def handle(args):
    start_date = args.startDay if args.startDay else datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    end_date = args.endtDay if args.endDay else datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]
    length = len(task_list)
    task_list.insert(
        {
            'startDt': start_date,
            'endDt': end_date,
        }
    )
    return task_list.find_one(id=length)
