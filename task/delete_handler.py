import dataset
from datetime import datetime

def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    end_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    task_list = db["taskList"]
    task_list.delete(id=args.id)
    return task_list.find_one(id=args.id)

