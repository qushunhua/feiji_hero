# coding:utf-8
from collections import Counter
def dubble_sort(list):
    n=len(list)
    for j in range(n-1):
        count=0
        for i in range(0,n-1-j):
            if list[i]<list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                count+=1
        if count==0:
            return


def getNumfromstr(str):
    slist=list(str)
    new_list=list(set(slist))
    result_dict={}
    for i in new_list:
        result_dict[i]=slist.count(i)
    print(sorted(result_dict.items(),key=lambda item:item[1],reverse=True))
    return result_dict

def study_counter(str):
    slist=list(str)
    counter=Counter()
    for i in slist:
        counter[i]+=1
    return dict(counter)


if __name__ == '__main__':

    str='sdfeidddass'
    print(getNumfromstr(str))
    # print(getNumfromstr(str))
    # list=[1,2,5,4,5,9,6,5,4,3,4]
    # print(len(list))
    # for i,k in enumerate(list):
    #     print("i{}:k{}".format(i,k))
    # dubble_sort(list)
    # print(list)
    # print(sorted(list,reverse=True))
    # print(reversed(list))
    # for i in reversed(list):
    #     print(i,end=' ')