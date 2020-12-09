# coding:utf-8
#定义节点
class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None
#定义链表
class Singlelinklist(object):
    '''单链表'''
    def __init__(self,node=None):
        self.__head=node
    def is_empty(self):
        '''判读是否为空'''
        return self.__head==None
    def length(self):
        '''获取链表长度'''
        cur=self.__head
        count=0
        while cur!=None:
            count+=1
            cur=cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur=self.__head
        print(cur.elem)
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next
        print("")
    def add(self,item):
        '''头部添加'''
        node=Node(item)
        node.next=self.__head
        self.__head=node
    def append(self,item):
        '''尾部添加'''
        node=Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur=self.__head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
    def insert(self,pos,item):
        '''指定位置插入元素'''
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre=self.__head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
            node=Node(item)
            node.next=pre.next
            pre.next=node
    def remove(self,item):
        '''删除节点'''
        cur=self.__head
        pre=None
        while cur!=None:
            if cur.elem==item:
                if cur==self.__head:
                    self.__head=cur.next
                else:
                    pre.next=cur.next
                break
            else:
                pre=cur
                cur=cur.next

    def search(self,item):
        '''查找节点是否存在'''
        cur=self.__head
        while cur!=None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        return False




if __name__ == '__main__':
    ll = Singlelinklist()
    ll.append(3)
    print(ll.travel())

    # print(ll.is_empty())
    # print(ll.length())
    #
    # ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())
    #
    # ll.append(2)
    # ll.add(8)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    # # 8 1 2 3 4 5 6
    # ll.insert(-1, 9)  # 9 8 1 23456
    # ll.travel()
    # ll.insert(3, 100)  # 9 8 1 100 2 3456
    # ll.travel()
    # ll.insert(10, 200)  # 9 8 1 100 23456 200
    # ll.travel()
    # ll.remove(100)
    # ll.travel()
    # ll.remove(9)
    # ll.travel()
    # ll.remove(200)
    # ll.travel()





