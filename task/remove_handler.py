import dataset
from pprint import pprint 

def handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    task_list = db["taskList"]

    result_set = task_list.find_one(id=args.id)
    target_row = [ item.get('id') for item in result_set]
    task_list.delete(id=args.id)
    return target_row
