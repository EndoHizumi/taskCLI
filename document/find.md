# find

```bash
find 
  -t, --taskName TASKNAME
  -p, --project PROJECT
  -c, --context CONTEXT
  -s, --startDay STARTDAY　date input format %Y/%m/%d %H:%M:%S
  -e, --endDay ENDDAY　date input format %Y/%m/%d %H:%M:%S
  -i, --importance {A,B,C,D,E}

```

## Description

display only match to the word.

## Examples

Example 1: display specified task name

```bash
python task.py find -t "test task"

ID taskName               startDt    endDt createAt            updateAt            project  tag      done  priority
-- --------               -------    ----- --------            --------            -------  ---      ----- --------
 1 test task                     　　　　　　2018/05/07 00:38:40 2018/05/07 00:38:40                   False (C)
```

Example 2: display specified task name

```bash
python task.py find -p "hoge project"

ID taskName               startDt    endDt createAt            updateAt            project       tag      done  priority
-- --------               -------    ----- --------            --------            -------       ---      ----- --------
 1 test task                     　　　　　　2018/05/07 00:38:40 2018/05/07 00:38:40 hoge project           False (C)
```
