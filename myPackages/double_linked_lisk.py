class Node:
    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class DLinklist():
    def __init__(self):
        self.header = None

    def is_empty(self):
        return self.header is None

    def length(self):
        if self.is_empty():
            return 0
        count = 0
        cur = self.header
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header.prev = node
            self.header = node

    # 在尾部追加
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.add(item)
        else:
            cur = self.header
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    # 在指定位置添加
    def insert(self, position, item):
        if position <= 0:
            self.add(item)
        if position >= self.length()-1:
            self.append(item)
        else:
            count = 0
            cur = self.header
            while count != position:
                count += 1
                cur = cur.next
            node = Node(item)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node

    # 遍历
    def traverse(self):
        if self.is_empty():
            return
        cur = self.header
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    # 查找
    def search(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.header
            while cur is not None:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next

    # 删除
    def remove(self, item):
        if self.is_empty():
            return
        if self.header.elem == item:
            if self.length() == 1:
                self.header = None
            else:
                self.header.next.prev = None
                self.header = self.header.next
            return
        cur = self.header.next
        while cur is not None:
            if cur.elem == item:
                if cur.next is not None:
                    cur.next.prev = cur.prev
                cur.prev.next = cur.next
                return
            else:
                cur = cur.next


if __name__ == '__main__':
    s = DLinklist()
    s.add(12)
    s.add(15)
    s.add(1)
    s.append(2)
    s.insert(2, 30)
    s.remove(15)
    s.traverse()

    print(s.search(1))


