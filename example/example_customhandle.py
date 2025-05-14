from exampleTimeLimit import TimeLimit
from time import time_ns as get_time
def get_ms() -> int:
    return get_time() / 1000000
def example():
    """示例"""
    def custom_handler(): # 自定义处理程序
        print("任务已超时（自定义处理程序）") # 打印超时信息
        exit() # 退出程序
    lim = TimeLimit(1000) # 限制1秒
    lim.set_custom_handler(custom_handler) # 设置自定义处理程序
    with lim as lim: # 开始计时
        for i in range(100000000): # 循环1亿次
            lim.checkpoint() # 检查点，这里会调用自定义处理程序
            print(i) # 打印i
            print(f"我们用了{get_ms() - lim.start}毫秒") # 打印我们用了多少毫秒
def main():
    example() # 运行示例
if __name__ == "__main__": # 如果是主程序
    main()