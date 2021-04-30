from queue import Queue


class PyQueue:
    def __init__(self):
        """
        初始化队列
        """
        self.queue_obj = Queue(maxsize=0)

    def en_queue(self, item):
        """
        入队列
        :param item:
        :return:
        """
        self.queue_obj.put(item)

    def del_queue(self):
        """
        出队列
        :return:
        """
        self.queue_obj.get()

    def get_size(self):
        """
        获取队列长度
        :return:
        """
        return self.queue_obj.qsize()

    def get_queue(self):
        """
        获取队列
        :return:
        """
        return self.queue_obj

queue = PyQueue()
queue.en_queue(2)
queue.en_queue(3)
queue.en_queue(4)
print(queue.get_size())
queue.del_queue()
print(queue.get_size())

