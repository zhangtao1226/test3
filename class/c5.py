def check_index(key):
    """
    指定的件是否是可接受的索引？
    键必须是非负整数，才是可接受的。
    如果不是整数，将引发TypeError异常；如果是负数，
    将引发IndexError异常（因为这个序列的长度是无穷的）
    :param key:
    :return:
    """
    if not isinstance(key, int): raise TypeError
    if key < 0 : raise IndexError

class ArithmeticSequence:
    def __init__(self, start = 0, step = 1):
        """
        初始化这个算术序列
        start 序列第一个值
        step 步长
        changed 一个字典，包含用户修改后的值
        :param start:
        :param step:
        """
        self.start = start
        self.step = step
        self.changed = {}
    def __getitem__(self, key):
        """
        从算术序列中获取一个元素
        :param key:
        :return:
        """
        check_index(key)
        try:
            print(key)
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        """
        修改算术序列中的元素
        :param key:
        :param value:
        :return:
        """
        check_index(key)
        print(value)
        self.changed[key] = value
        print(self.changed)

s = ArithmeticSequence(1, 2)

s[4]=2