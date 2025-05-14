from time import time_ns as get_time
def get_ms() -> int:
    return get_time() / 1000000
class TimeLimit:
    """限制一个任务的最大执行时间"""
    def __init__(self, lim: float) -> None:
        self.lim = lim
        self.start = 0
        self.playing = False
        self.custom_handler = None
    def checkpoint(self) -> bool:
        """检查点"""
        if not self.playing:
            return True
        if get_ms() - self.start > self.lim:
            self.playing = False
            if self.custom_handler:
                self.custom_handler()
            else:
                raise TimeoutError("任务已超时")
            self.__exit__()
            return False
        return True
    def set_custom_handler(self, handler: callable) -> None:
        """设置自定义处理程序"""
        self.custom_handler = handler
    def __enter__(self) -> "TimeLimit":
        self.playing = True
        self.start = get_ms()
        return self
    def __exit__(self, _1, _2, _3) -> None:
        self.playing = False