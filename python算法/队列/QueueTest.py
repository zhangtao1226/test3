
class QueueTest:
    def __init__(self):
        self.list = []

    def is_empty(self):
        """
        判断当前队列是否为空
        :return:
        """
        return self.list == []

    def enqueue(self, item):
        """
        入队列
        :param item:
        :return:
        """
        if item is None:
            return
        self.list.append(item)
        return self.list

    def dequeue(self):
        """
        出队列
        :return:
        """
        self.list.pop(0)
        return self.list

    def size_queue(self):
        """
        队列长度
        :return:
        """
        return len(self.list)


queue = QueueTest()
print(queue.enqueue(2))