# coding:utf-8

class Queue(object):
    def __init__(self):
        self.__list=[]
    def in_queue(self,item):
        self.__list.append(item)
    def out_queue(self):
        return self.__list.pop(0)
    def is_empty(self):
        return self.__list==[]
    def get_size(self):
        return len(self.__list)



if __name__ == '__main__':
    q=Queue()
    q.in_queue(1)
    q.in_queue(2)
    q.in_queue(3)
    q.in_queue(4)
    q.in_queue(5)
    print(q.out_queue())
    print(q.out_queue())
    print(q.out_queue())
    print(q.out_queue())
    print(q.out_queue())
    print(q.is_empty())
    print(q.get_size())