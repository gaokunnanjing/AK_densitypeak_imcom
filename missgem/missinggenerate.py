from random import random

import numpy as np

#输入原文件加载路径和结果保存路径以及数据名,输出缺失文件
from ismember import ismember

from 论文实验.AK_densitypeak_imcom.missgem.generateabsentmatrix import Generateabsentmatrix
from 论文实验.AK_densitypeak_imcom.missgem.nanfilling import Nanfilling
def combine(absentmatrix, c_data, nochoice, choice):
    N=len(nochoice)+len(choice)
    outdata=np.zeros([N,np.shape(absentmatrix)[1]])
    i=0
    for index in nochoice:
        outdata[index]=absentmatrix[i]
        i+=1
    i=0
    for index in choice:
        outdata[index]=c_data[i]
        i+=1
    return outdata
#并不是完全按缺失率随机生成,而是先选出一部分行作为完全数据集,然后再剩下一部分行制造缺失
def missGen(loadpath,resultpath,dataname):
    readpath=loadpath+ '\\'+ dataname+ '\\'+dataname +'_dataset.txt'
    originmatrix = np.loadtxt(readpath);

    data=originmatrix[:,1:]  #除去标签
    sample, dimension =np.shape(data)[0],np.shape(data)[1];

    choice=np.random.choice(sample,int(sample*0.5),False)  #保证一定程度的完整数据
    c_data=data[choice,:]#选出的完整数据
    total=[i for i in range(sample)]
    nochoice=np.setdiff1d(total,choice)
    ic_data=data[nochoice,:]
    ratio = [0.05,0.1,0.15,0.2,0.25];
    # ratio = [ 0.15];
    for iter in range(len(ratio)):

        missingindex = Generateabsentmatrix(ic_data, ratio[iter]*len(total)/len(nochoice)); # 产生缺失矩阵
        absentmatrix = Nanfilling(ic_data, missingindex); # 将缺失矩阵填充为nan

        outdata=combine(absentmatrix,c_data,nochoice,choice)

        writepath=resultpath+'\\'+  dataname+'\\'+  dataname+  '_missing_'+  str(ratio[iter] * 100)+  '.txt'
        np.savetxt(writepath, outdata)
    # print(originmatrix)

#读入数据,改变列顺序,使第1列是标签,然后再组装保存
def changedata(loadpath, dataname):
    readpath = loadpath + '\\' + dataname + '\\' + dataname + '_dataset.txt'
    originmatrix = np.loadtxt(readpath);

    data = originmatrix[:, :-1]  # 除去标签
    label=originmatrix[:, -1]
    new_originmatrix=np.c_[label,data]
    writepath= loadpath + '\\' + dataname + '\\' + dataname + '_datasetnew.txt'
    np.savetxt(writepath, new_originmatrix)


if __name__ == "__main__":
    # changedata('G:\\pythonSpace\\论文实验\\AK_densitypeak_imcom\\dataset', 'flame')
    missGen('G:\\pythonSpace\\论文实验\\AK_densitypeak_imcom\\dataset', 'G:\\pythonSpace\\论文实验\\AK_densitypeak_imcom\\dataset', 'PenDigits')

     # ratio = [0.1, 0.15, 0.2, 0.25];
    # writepath = 'G:\\pythonSpace\\论文实验\\AK_densitypeak_imcom\\dataset'+ '\\' + 'five_cluster' + '\\' + 'five_cluster'+ '_missing_' + str(ratio[3] * 100) + '.txt'
    # aaa=np.loadtxt(writepath)
    # a=np.arange(0,12,0.5).reshape(4,-1)
    # np.savetxt('a.txt',a)
    # a=np.loadtxt("a.txt")
    # Row wise comparison
    # a_vec = np.array(([1, 2, 3], (4, 5, 6), (7, 8, 9), (10, 11, 12)))
    # b_vec = np.array(((4, 5, 6), (7, 8, 0)))
    # a_vec = np.array([[4, 5, 7]])
    # b_vec = np.array([ [1, 2, 3],[4, 5, 6], [7, 8, 9], [10, 11, 12]])
    # res = ismember(a_vec, b_vec, 'rows')
   # a_vec[Iloc] == b_vec[idx]
    print('hi')
