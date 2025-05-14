from exampleTimeLimit import TimeLimit
from time import time_ns as get_time
def get_ms() -> int:
    return get_time() / 1000000
def example():
    """示例"""
    lim = TimeLimit(1000) # 限制1秒
    with lim as lim: # 开始计时
        for i in range(100000000): # 循环1亿次
            try:
                lim.checkpoint() # 检查点
            except TimeoutError: # 如果超时
                print("任务已超时") # 打印超时信息
                break # 跳出循环
            print(i) # 打印i
            print(f"我们用了{get_ms() - lim.start}毫秒") # 打印我们用了多少毫秒
def main():
    example() # 运行示例
if __name__ == "__main__": # 如果是主程序
    main()