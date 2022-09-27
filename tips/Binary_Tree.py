class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        # 현재 root node를 지정.
        self.current_node = self.root
        while True:
            # 삽입하는 값이 기존의 root node 보다 작으면 왼쪽
            if value < self.current_node.value:
                # 다만 왼쪽이 더 작아야 함.
                if self.current_node.left != None:
                    self.current_node = self.current_noce.left
                else:
                    self.current_node.left = Node(value)
                    break
            # 만일 삽입하는 값이 기존의 root보다 크면 오른쪽
            else:
                # 넣을때 있는지 없는지 확인하고 넣기.
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
