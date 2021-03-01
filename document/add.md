# Add-Task

```bash
Add-Task alias:add
[-taskName] <String>
[-startDay] <String>
[-endDay] <String>
[-priority] <String>
[-context] <String>
[-projectName] <String>
```

## Description

Insert task to TaskList.
If priority is omitted, priority medium is set. 

## Examples

Example1: add task "Test task"

```bash
task Add-Task "Test task"

ID taskName               startDt    endDt createAt            updateAt            project  tag      done priority
-- --------               -------    ----- --------            --------            -------  ---      ----- --------
 1 test task                     　　　　　　2018/05/07 00:38:40 2018/05/07 00:38:40                   False (C)
```

Example2: add task "Test task" append start Date

```bash
task Add-Task "Test task" --startDay "2018/05/05"

ID taskName               startDt    endDt createAt            updateAt            project  tag      done priority
-- --------               -------    ----- --------            --------            -------  ---      ----- --------
 1 test task              2018/05/05       2018/05/14 23:30:40 2018/05/14 23:30:40                   False (C)
```

Example3: add task "Test task" append start Date and end Date

```bash
task Add-Task "Test task" -startDay "2018/05/05" -endDay "2018/05/05"

ID taskName               startDt    endDt      createAt            updateAt            project  tag      done priority
-- --------               -------    -----      --------            --------            -------  ---      ----- --------
 1 taskname               2018/05/14 2018/05/05 2018/05/14 23:33:08 2018/05/14 23:33:08                   False (C)

```

Example4: add task "Test task" apeend priority

```bash
task Add-Task "Test task" -priority "(A)"

ID taskName               startDt    endDt      createAt            updateAt            project  tag      done priority
-- --------               -------    -----      --------            --------            -------  ---      ----- --------
 1 Test task　　　　　                          　2018/05/14 23:34:45 2018/05/14 23:34:45                   False (A)

```

Example5: add task "Test task" apeend project

```bash
task Add-Task "Test task" -project "testProject"

ID taskName               startDt    endDt      createAt            updateAt            project  tag      done priority
-- --------               -------    -----      --------            --------            -------  ---      ----- --------
 1 Test task　　　　　                          　2018/05/14 23:38:01 2018/05/14 23:38:01 @testProject              False (C)

```

Example6: add task "Test task" apeend Context

```bash
task Add-Task "Test task" -tag "review"

ID taskName               startDt    endDt      createAt            updateAt            project      tag          done priority
-- --------               -------    -----      --------            --------            -------      ---          ----- --------
 1 Test task　　　　　                          　2018/05/14 23:39:08 2018/05/14 23:39:08              review      False (A)

```