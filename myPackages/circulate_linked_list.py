class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinCyclinkedlist():
    def __init__(self):
        self.header = None

    def is_empty(self):
        return self.header == None

    def length(self):
        if self.is_empty():
            return 0
        count = 0
        cur = self.header
        while cur.next != self.header:
            count = count + 1
            cur = cur.next
        count += 1
        return count

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.header = node
            node.next = node
        else:
            cur = self.header
            node.next = cur
            while cur.next != self.header:
                cur = cur.next
            node.next = self.header
            self.header = node
            cur.next = node

    # 在尾部追加
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.add(item)
        else:
            cur = self.header
            while cur.next != self.header:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    # 在指定位置添加
    def insert(self, position, item):
        node = Node(item)
        if position <= 0:
            self.add(item)
        elif position >= self.length() - 1:
            self.append(item)
        else:
            count = 0
            cur = self.header
            while count < position - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def traverse(self):
        if self.is_empty():
            return
        cur = self.header
        while cur.next != self.header:
            print(cur.elem, end=' ')
            cur = cur.next
        print(cur.elem)

    def search(self, item):
        if self.is_empty():
            return False
        else:
            cur = self.header
            while cur.next != self.header:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            if cur.elem == item:
                return True
            return False

    def remove(self, item):
        if self.is_empty():
            return
        if self.header.elem == item:
            if self.length() == 1:
                self.header = None
            else:
                h = self.header
                while h.next != self.header:
                    h = h.next
                self.header = self.header.next
                h.next = self.header
            return
        cur = self.header
        # pre = cur
        while cur.next != self.header:
            if cur.next.elem == item:
                cur.next = cur.next.next
                return
            else:
                # pre = cur
                cur = cur.next
        # if cur.elem == item:
            # pre.next = cur.next


if __name__ == '__main__':
    s = SinCyclinkedlist()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.append(5)
    s.insert(2,6)
    s.remove(2)
    s.traverse()
    print(s.length())
    print(s.search(5))
