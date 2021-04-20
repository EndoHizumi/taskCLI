import dataset
from datetime import datetime

def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    end_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    task_list = db["taskList"]
    task_list.update({'id': args.id, 'state': 1, 'endDt': end_date, 'updateAt': end_date, 'tag': 'done'}, ['id'])
    return task_list.find_one(id=args.id)
