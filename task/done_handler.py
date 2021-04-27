import dataset
import os
import subprocess
from datetime import datetime

prehookFilePath = './hook/pre-add-hook'
posthookFilePath = './hook/post-add-hook'


def prehook():
    if os.path.exists(prehookFilePath):
        subprocess.run(prehookFilePath)


def posthook():
    if os.path.exists(posthookFilePath):
        subprocess.run(posthookFilePath)


def _handle(args):
    db = dataset.connect("sqlite:///taskList.sqlite")
    end_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    task_list = db["taskList"]
    task_list.update({'id': args.id, 'state': 1, 'endDt': end_date, 'updateAt': end_date, 'tag': 'done'}, ['id'])
    return task_list.find_one(id=args.id)


def handle(args):
    prehook()
    _handle(args)
    posthook()
