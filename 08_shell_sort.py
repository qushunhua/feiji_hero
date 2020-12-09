# coding: utf-8

def shell_sort(alist):
    n=len(alist)
    gap=n//2
    print(gap)
    while gap>0:
        for j in range(gap,n):
            i=j
            while i>0:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=gap
                else:break
        gap//=2

quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])


if __name__ == '__main__':
    alist=[21,3,1,2,5,44,67,9]
    shell_sort(alist)
    print(alist)