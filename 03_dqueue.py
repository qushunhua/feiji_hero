# coding:utf-8

class Dqueue(object):
    def __init__(self):
        self.__list=[]

    def in_head(self,item):
        self.__list.insert(0,item)

    def in_tail(self,item):
        self.__list.append(item)

    def out_head(self):
        return self.__list.pop(0)

    def out_tail(self):
        return self.__list.pop(-1)

    def is_empty(self):
        return self.__list==[]
    def get_size(self):
        return len(self.__list)



if __name__ == '__main__':
    q=Dqueue()
    q.in_tail(1)
    q.in_tail(2)
    q.in_tail(3)
    q.in_tail(4)
    print(q.out_tail())
    print(q.out_tail())
    print(q.out_tail())
    print(q.out_tail())
    print(q.is_empty())
    print(q.get_size())