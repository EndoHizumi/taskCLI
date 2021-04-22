import dataset
from datetime import datetime

def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    start_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    task_list = db["taskList"]
    task_list.update({'id': args.id, 'state': 0, 'startDt': None, 'endDt': None, 'updateAt': start_date, 'tag': 'todo'}, ['id'])
    return task_list.find_one(id=args.id)
