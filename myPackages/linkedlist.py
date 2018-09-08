class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Singlelinked:
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
            count = count + 1
            cur = cur.next
        return count

    # 在头部添加
    def add(self, item):
        node = Node(item)   # 创建节点
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node

    # 在尾部添加
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.add(item)
        else:
            cur = self.header
            while cur.next is not None:
                cur = cur.next
            # 此时指针指向最后一个元素
            cur.next = node

    # 在指定位置添加
    def insert(self, position, item):
        node = Node(item)
        if position <= 0:
            self.add(item)
        elif position >= (self.length() - 1):
            self.append(item)
        else:
            count = 0
            cur = self.header
            while count < position - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def traverse(self):
        if self.is_empty():
            return
        else:
            cur = self.header
            while cur is not None:
                print(cur.elem, end=' ')
                cur = cur.next
        print()

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.header
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        if self.is_empty():
            return
        if self.header.elem == item:
            if self.length() == 1:
                self.header = None
            else:
                self.header = self.header.next
        else:
            cur = self.header
            while cur is not None:
                if cur.next is not None and cur.next.elem == item:
                    cur.next = cur.next.next
                    break
                else:
                    cur = cur.next


if __name__ == '__main__':
    s = Singlelinked()
    print(s.is_empty())
    print(s.length())
    s.add(1)
    s.add(2)
    s.add(3)
    s.append(4)
    s.traverse()
    print(s.search(4))
    # s.remove(4)
    s.traverse()
    print(s.length())
