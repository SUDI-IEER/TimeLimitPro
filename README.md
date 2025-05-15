# 介绍
![GitHub License](https://img.shields.io/github/license/LesBoys43/TimeLimitPro?style=plastic) ![GitHub branch status](https://img.shields.io/github/checks-status/LesBoys43/TimeLimitPro/master?style=plastic)
这是一个简单的 Python 任务时间限制工具 可以轻松限制复杂任务的最高用时
# 使用
## 一般使用
```python
# 首先，初始化一个 TimeLimit 对象，并传入最高用时（毫秒）
limit = TimeLimit(1000)  # 1 秒
# 然后，使用 with 语句来限制任务的执行时间
with limit:
    try:
        # 在任务中插入一些检查点
        limit.checkpoint() # 不触发
    except TimeoutError:
        print("任务超时！")
        # 在这里处理超时后的逻辑
    # 在这里编写需要限制时间的代码
    time.sleep(1.5) # 模拟耗时操作
    try: # 在任务中插入一些检查点
        limit.checkpoint() # 触发
    except TimeoutError:
        print("任务超时！")
        # 在这里处理超时后的逻辑
```
## 自定义处理程序
```python
# 定义一个自定义的处理程序
def custom_handler():
    print("任务超时！")
    # 在这里处理超时后的逻辑
# 初始化一个 TimeLimit 对象，并传入最高用时（毫秒）和自定义处理程序
limit = TimeLimit(1000)  # 1 秒
limit.set_custom_handler(custom_handler)  # 在初始化后设置自定义处理程序
# 然后，使用 with 语句来限制任务的执行时间
with limit:
    # 在任务中插入一些检查点
    limit.checkpoint() # 不触发
    # 在这里编写需要限制时间的代码
    time.sleep(1.5) # 模拟耗时操作
    limit.checkpoint() # 触发
```
