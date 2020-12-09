# coding: utf-8

def insert_sort(alist):
    n=len(alist)
    for j in range(1,n):
        i=j
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            else:
                break


if __name__ == '__main__':
    # alist=[1,2,1,2,33,22,2,4,12]
    # insert_sort(alist)
    # print(alist)
    slist = [12,32,43,23,54,34,5,43,45,67,56,57,76,8,67,87,88,98,99,69,774]
    print(len(slist))
    i=0
    while i<5:
        dlist=slist[i::5]
        i += 1
        print(dlist)