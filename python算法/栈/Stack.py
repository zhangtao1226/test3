
class Stack:
    def __init__(self):
        """
        初始化，并创建空栈
        """
        self.stack = []

    def __len__(self):
        """
        返回栈长度
        :return:
        """
        return len(self.stack)

    def is_empty(self):
        """
        返回栈是否为空栈
        :return:
        """
        return self.stack == []

    def push(self, item):
        """
        向栈顶压入一个元素
        :param item:
        :return:
        """
        self.stack.append(item)

    def get_top(self):
        """
        获取栈顶元素
        :return:
        """
        if self.is_empty():
            return 'Stack is empty'
        return self.stack[-1]

    def pop(self):
        """
        执行出栈，并返回出栈元素
        :return:
        """
        if self.is_empty():
            return 'Stack is empty'
        return self.stack.pop()