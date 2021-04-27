"""
创建节点
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singlelink:
    def __init__(self):
        self.head = None
        self.length = 0
        return

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        if self.head is None:
            return True
        else:
            return False


    def append_node(self, node):
        """
        向链表中添加节点
        :param node:
        :return:
        """
        current_node = self.head
        if self.is_empty():
            self.head = node
            self.length += 1
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
            self.length += 1

    def insert_node(self, index, data):
        """
        插入节点到链表中
        :param data:
        :return:
        """
        if self.is_empty():
            print("this link is empty")
            return

        if index < 0:
            print("error: out in index!")
            return
        item = Node(data)
        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return
        node_index = 0
        node = self.head
        prev = self.head
        while node.next and node_index < index:
            prev = node
            node = node.next
            node_index += 1

            if node_index == index:
                item.next = node
                prev.next = item
                self.length += 1

        if index >= self.length:
            self.append_node(item)
            return

    def find_node(self, value):
        """
        通过数值查找节点,并返回节点id
        :param value:
        :return:
        """
        current_node = self.head
        node_id = 1
        result = []
        while current_node is not None:
            if current_node.data == value:
                result.append(node_id)
            current_node = current_node.next
            node_id += 1
        return result

    def delete_node_byId(self, item_id):
        """
        通过节点ID，删除节点
        :param item_id:
        :return:
        """
        node_id = 1
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if node_id == item_id:
                if prev_node is not None:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                self.length -= 1

            prev_node = current_node
            current_node = current_node.next
            node_id += 1
        return



    def print_link(self):
        """
        打印链表
        :return:
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return


Node1 = Node(1)
Node2 = Node(4)
Node3 = Node(2)
Node4 = Node(6)

link = Singlelink()
for node in [Node1, Node2, Node3, Node4]:
    link.append_node(node)
# link.insert_node(1, 6)
link.print_link()
node = link.find_node(4)
print(node)

for node_id in node:
    link.delete_node_byId(node_id)

link.print_link()