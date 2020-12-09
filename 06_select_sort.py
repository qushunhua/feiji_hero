# coding:utf-8

def select_sort(alist):
    n=len(alist)
    for j in range(0,n-1):
        min_index=j
        for i in range(j+1,n-1):
            if alist[min_index]>alist[i]:
                min_index=i
        alist[min_index],alist[j]=alist[j],alist[min_index]


#判断回文字符串
def is_palindromic2(num):
    count = 0
    for i in range(len(num)):
        if count < len(num) // 2:
            if num[i] != num[len(num) - i - 1]:#num[6],#num[0]
                return False
        else:
            break
        count += 1
    return True
if __name__ == '__main__':
    num='abcfcoa'
    print(num[1])
    print(num[len(num)-1-1])
    print(is_palindromic2(num))
