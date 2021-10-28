import numpy as np

from 论文实验.AK_densitypeak_imcom.missgem.nanfilling import Nanfilling

#检查A 是否与missingindex某行重复
def check(A, param):
    c=(A==param)
    return c.all()
def ismember(A, missingindex):
    N,S=np.shape(missingindex)[0],np.shape(missingindex)[1]
    for row in range(N):
        res=check(A,missingindex[row])
        if res==True:
            return True
    return False


def checkallcolmiss(missingindex, data, dimension):
    missingindex = np.unique(missingindex, axis=0);
    data2 = Nanfilling(data, missingindex);
    a = np.isnan(data2)
    nannumber = np.sum(np.isnan(data2), axis=1);
    if (dimension in nannumber) == True:
        return True

def Generateabsentmatrix(data, ratio):
    sample,dimension = np.shape(data)[0],np.shape(data)[1];
    num = int(np.ceil(sample*dimension*ratio))#总缺失数
    missingindex = np.ones([num,2]).astype(int)
    missingindex=-missingindex
    flag = 1;
    flag2 =1;
    while flag == 1 or flag2 == 1:
        i=0;

        while i!= (num):
    #         s = RandStream('mt19937ar','seed','shuffle');
    #         RandStream.setGlobalStream(s);
            m = np.random.randint(0,sample); #随机选1行
            n = np.random.randint(0,dimension); #随机选1列
            A=np.array([m,n]).reshape([-1,2])
            res=ismember(A,missingindex)
            if ismember([m,n],missingindex) == False: #如果m和n不在缺失矩阵里,把它加到缺失矩阵

                missingindex[i,0] = m;
                missingindex[i,1] = n;
                if checkallcolmiss(missingindex,data,dimension):  #如果检查到让m行n列缺失会造成整行缺失,那么不允许
                    missingindex[i, 0] = -1;
                    missingindex[i, 1] = -1;
                    continue
                i = i+1;

        a,b = np.shape(np.unique(missingindex,axis=0))[0],np.shape(np.unique(missingindex,axis=0))[1];#unique函数返回所有独特的行
        if a == num:
            flag =0;
            missingindex = np.unique(missingindex,axis=0);
            data2 = Nanfilling(data,missingindex);
            a=np.isnan(data2)
            nannumber = np.sum(np.isnan(data2),axis=1);
            if (dimension in nannumber) == False:
                flag2 =0;

    return missingindex


# function [missingindex] = generateabsentmatrix( data,ratio )
# %UNTITLED6 此处显示有关此函数的摘要
# %   此处显示详细说明
# [sample,dimension] = size(data);
# num = ceil(sample*dimension*ratio);%总缺失数
# missingindex = zeros(num,2);
# flag = 1;
# flag2 =1;
#
# while flag == 1 || flag2 == 1
#     i=1;
#     while i~= (num+1)
# %         s = RandStream('mt19937ar','seed','shuffle');
# %         RandStream.setGlobalStream(s);
#         m = randi(sample-1,1)+1; %随机选1行
#         n = randi(dimension,1); %随机选1列
#
#         if ismember([m,n],missingindex,'rows') == 0 %如果m和n不在缺失矩阵里,把它加到缺失矩阵
#             missingindex(i,1) = m;
#             missingindex(i,2) = n;
#             i = i+1;
#         end
#     end
#     [a,b] = size(unique(missingindex,'rows'));%unique函数返回所有独特的行
#     if a == num
#         flag =0;
#         missingindex = unique(missingindex,'rows');
#         data2 = nanfilling(data,missingindex);  %
#         nannumber = sum(isnan(data2),2);
#         if ismember(dimension,nannumber) == 0
#             flag2 =0;
#             missingindex = unique(missingindex,'rows');
#         end
#     end
#
#
#
# end