# taskCLI

## Overview

task is Todo List manager on CLI

## setup

require python 3.8 or later

```
$ pip install -r requirements.txt
```

## usage

 ```task.py [-h] {add,done,show}```

## arguments

    add            Insert task to TaskList. If priority is omitted, priority medium is set.
    done           Done to task
    show           show taskList
    -h, --help       show this help message and exit

## sub command

### add

usage: task.py add [-h] -t TASKNAME

optional arguments:
  -h, --help            show this help message and exit
  -t TASKNAME, --taskName TASKNAME

### done

usage: task.py done [-h] -i ID

optional arguments:
  -h, --help      show this help message and exit
  -i ID, --id ID

### show

usage: task.py show [-h]

optional arguments:
  -h, --help  show this help message and exit
