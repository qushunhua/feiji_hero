# coding:utf-8

def quick_sort(alist,first,last):
    if first>=last:
        return
    mid_value=alist[first]
    low=first
    high=last
    while low<high:
        while low<high and alist[high]>=mid_value:
            high-=1
        alist[low]=alist[high]
        while low<high and alist[low]<mid_value:
            low+=1
        alist[high]=alist[low]
    #退出整个循环的时候，将找到mid_value的位置，low=high
    alist[low]=mid_value
    #对low左边排序（low移动到mid_value位置）
    quick_sort(alist,first,low-1)
    #对右边排序
    quick_sort(alist,low+1,last)

def jiecheng(n):
    if n==1:
        return 1
    else:return n*jiecheng(n-1)

if __name__ == '__main__':
    # alist=[11,2,1,33,4,53,42,3,1]
    # quick_sort(alist,0,len(alist)-1)
    # print(alist)
    print(jiecheng(3))